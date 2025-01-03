from __future__ import annotations

import importlib
import inspect
import logging
from pathlib import Path
from typing import Callable

import narwhals as nw
from narwhals.typing import IntoFrame

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class DataSet:
    def __into_narwahlframe__(self, frame: IntoFrame) -> IntoFrame:
        """Convert a native frame to a narwhals frame."""
        return nw.from_native(frame)

    def __init__(self, frame: IntoFrame) -> None:
        self.results: dict[str, str | dict[str, str | None | bool | list[str]]] = {
            "Summary": {
                "passed": None,
                "validations": "No validation checks were added.",
            },
        }
        self.frame = self.__into_narwahlframe__(frame)
        self.__generate_validation_attributes__()

    def __generate_validation_attributes__(self) -> None:
        validoopsie_dir = Path(__file__).parent
        oops_catalogue_dir = validoopsie_dir / "validation_catalogue"

        # Get list of subdirectories in validation_catalogue
        subdirectories = [d for d in oops_catalogue_dir.iterdir() if d.is_dir()]

        for subdir in subdirectories:
            subclass_name = subdir.name
            SubClass = type(subclass_name, (), {})

            # List of Python files in the subdirectory, excluding __init__.py
            py_files = [f for f in subdir.glob("*.py") if f.name != "__init__.py"]

            for py_file in py_files:
                # Get module name including package
                module_relative_path = py_file.relative_to(validoopsie_dir.parent)
                module_name = ".".join(module_relative_path.with_suffix("").parts)

                # Import the module from the file path
                spec = importlib.util.spec_from_file_location(
                    module_name,
                    py_file,
                )
                module = importlib.util.module_from_spec(spec)
                if spec.loader:
                    spec.loader.exec_module(module)
                else:
                    logging.warning(
                        f"Could not load module {module_name} from {py_file}",
                    )
                    continue

                # Find classes defined in the module
                classes_in_module = inspect.getmembers(
                    module,
                    lambda member: inspect.isclass(member)
                    and member.__name__.lower() == py_file.stem.replace("_", "").lower(),
                )

                for _, class_obj in classes_in_module:
                    # Attach the method to the subclass
                    setattr(
                        SubClass,
                        py_file.stem,
                        self.__make_validation_method__(class_obj),
                    )

            # Attach the subclass to the DataSet instance
            setattr(self, subclass_name, SubClass())

    def __make_validation_method__(self, class_obj):
        def validation_method(*args, **kwargs):
            return self.__create_validation_method__(
                class_obj,
                *args,
                **kwargs,
            )

        return validation_method

    def __create_validation_method__(
        self,
        validation_class: Callable[...],
        *args: str | list[str | int] | int,
        **kwargs: str | list[str | int] | int,
    ) -> DataSet:
        args = args[1:]
        test = validation_class(*args, **kwargs)
        result = test.execute_check(frame=self.frame)
        status = result["result"]["status"]
        name = f"{test.__class__.__name__}_{test.column}"
        # If the validation check failed, set the overall result to fail
        # If No validations are added, the result will be None
        # If all validations pass, the result will be PASS
        if status == "Fail":
            self.results["Summary"]["passed"] = False
        elif self.results["Summary"]["passed"] is None and status == "Success":
            self.results["Summary"]["passed"] = True

        if isinstance(self.results["Summary"]["validations"], str):
            self.results["Summary"]["validations"] = [name]
        else:
            self.results["Summary"]["validations"].append(name)

        self.results.update({name: result})
        return self

    def validate(self) -> DataSet | None:
        """Validate the data set."""
        if self.results == {}:
            msg = "No validation checks were added."
            raise ValueError(msg)
        failed_oopsies: list[str] = []
        for key in self.results:
            # Skip the overall result, as it is not a validation check
            if key == "Summary":
                continue

            # Check if the validation failed and if it is high impact then it
            # should raise an error
            failed = self.results[key]["result"]["status"] == "Fail"
            high_impact = self.results[key]["impact"].lower() == "high"
            medium_impact = self.results[key]["impact"].lower() == "medium"

            if failed and high_impact:
                failed_oopsies.append(key)
                warning_msg = (
                    f"Failed validation: {key} - {self.results[key]['result']['message']}"
                )
                logging.critical(warning_msg)
            elif failed and medium_impact:
                warning_msg = (
                    f"Failed validation: {key} - {self.results[key]['result']['message']}"
                )
                logging.warning(warning_msg)
            elif failed:
                warning_msg = (
                    f"Failed validation: {key} - {self.results[key]['result']['message']}"
                )
                logging.error(warning_msg)
            else:
                info_msg = f"Passed validation: {key}"
                logging.info(info_msg)
        if failed_oopsies:
            value_error_msg = f"Validation failed: {failed_oopsies}"
            raise ValueError(value_error_msg)
