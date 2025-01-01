import argparse
import importlib.util
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        prog="ouro",
        description="Generates GitHub Actions workflows from the ouro DSL"
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommands")
    synth_parser = subparsers.add_parser("synth", help="Generate the GitHub Actions workflow")


    synth_parser.add_argument(
        "--file",
        "-f",
        default="ouro_workflow.py",
        help="The file containing the ouro workflow definition",
    )

    synth_parser.add_argument(
        "--func",
        "-u",
        default="synth_workflow",
        help="The function to call to generate the workflow",
    )

    synth_parser.add_argument(
        "--output",
        "-o",
        default="github/workflows/ci.yml",
        help="The output path for the GitHub Actions workflow",
    )

    args = parser.parse_args()

    if not os.path.exists(args.file):
        sys.exit(f"Could not find file {args.file}")

    # Load the module and call the function to generate the workflow
    mod_name = os.path.splitext(os.path.basename(args.file))[0]
    spec = importlib.util.spec_from_file_location(mod_name, args.file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if not hasattr(mod, args.func):
        sys.exit(f"Function {args.func} not found in {args.file}")

    workflow = getattr(mod, args.func)()

    # Ensure that the object has a to_yaml method
    if not hasattr(workflow, "to_yaml") or not callable(workflow.to_yaml):
        sys.exit(f"Workflow object must have a to_yaml method")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    with open(args.output, "w") as f:
        f.write(workflow.to_yaml())

    print(f"Workflow written to {args.output}")


if __name__ == "__main__":
    main()
