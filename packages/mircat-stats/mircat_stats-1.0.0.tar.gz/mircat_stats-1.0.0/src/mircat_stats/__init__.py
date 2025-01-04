import argparse
from loguru import logger
from pathlib import Path
from mircat_stats.configs.logging import configure_logging
from mircat_stats.configs import set_num_threads
from threadpoolctl import threadpool_limits
from mircat_stats.dicom import convert_dicom_folders_to_nifti, update
from mircat_stats.statistics import calculate_nifti_stats


def mircat_stats():
    """
    MirCAT Stats Only CLI tool
    """
    parser = argparse.ArgumentParser(description="Mircato Stats Only CLI tool")
    parser.add_argument("-q", "--quiet", help="Decrease output verbosity", action="store_true")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create the 'convert' subparser
    convert_parser = subparsers.add_parser("convert", help="Convert DICOM files")
    convert_parser.add_argument("dicoms", help="Path to DICOM files", type=Path)
    convert_parser.add_argument("output_dir", help="Output directory", type=Path)
    convert_parser.add_argument("-n", "--num-workers", help="Number of something", type=int, default=1)
    convert_parser.add_argument(
        "-ax",
        "--axial-only",
        help="Only convert axial dicom series",
        action="store_true",
    )
    convert_parser.add_argument("-nm", "--no-mip", help="Do not convert likely mip series", action="store_true")
    convert_parser.add_argument(
        "-th",
        "--threads",
        help="Number of threads for each worker",
        type=int,
        default=1,
    )
    # Set up stats parser
    stats_parser = subparsers.add_parser("stats", description="Calculate statistics for NIfTI files")
    stats_parser.add_argument(
        "niftis",
        type=Path,
        help="NIfTI file or a text file containing paths to multiple NIfTI files to calculate statistics for",
    )
    stats_parser.add_argument(
        "-t",
        "--task-list",
        type=str,
        nargs="+",
        default=["total", "contrast", "aorta", "tissues"],
        help='List of statistics tasks to perform. Default = ["total", "contrast", "aorta", "tissues"]',
    )
    stats_parser.add_argument(
        "-n",
        "--num-workers",
        type=int,
        default=4,
        help="Number of workers to use for multi-process operations. Default=1",
    )
    stats_parser.add_argument(
        "-th",
        "--threads",
        type=int,
        default=4,
        help="Number of threads each worker will use. Default=4",
    )
    stats_parser.add_argument(
        "-mc",
        "--mark-complete",
        action="store_true",
        help="Mark the statistics as complete regardless of stats performed",
    )
    stats_parser.add_argument(
        "-g",
        "--gaussian",
        action="store_true",
        help="Apply a gaussian smoothing to the label segmentations. Will be slower but more precise upon scaling",
    )
    # Create update parser
    update_parser = subparsers.add_parser(
        "update",
        help="Update the header and stats data for a NIfTI file to the latest version",
    )
    update_parser.add_argument("niftis", help="Path to NIfTI files", type=Path)
    update_parser.add_argument("-n", "--num-workers", help="Number of workers", type=int, default=1)
    update_parser.add_argument("-th", "--threads", help="Number of threads", type=int, default=1)

    args = parser.parse_args()
    args.verbose = not args.quiet
    set_num_threads(args.threads)
    threadpool_limits(limits=args.threads)
    if args.command == "convert":
        if args.dicoms.is_dir():
            logfile = "./nifti_conversion_log.json"
            dicom_list = [str(args.dicoms)]
        else:
            logfile = f'{args.dicoms.with_suffix("")}_conversion_log.json'
            with args.dicoms.open() as f:
                dicom_list = f.read().splitlines()
        configure_logging(logfile, args.verbose)
        convert_dicom_folders_to_nifti(
            dicom_list,
            args.output_dir,
            args.num_workers,
            args.axial_only,
            args.no_mip,
            args.verbose,
        )

    elif args.command == "stats" or args.command == "update":
        # If the input to the niftis argument is just a singular nifti file, make it a list and log in the same dir
        if args.niftis.suffixes == [".nii", ".gz"] or args.niftis.suffix == ".nii":
            logfile = str(args.niftis).replace(".nii", "").replace(".gz", "")
            logfile = f"{logfile}_{args.command}_log.jsonl"
            nifti_list = [str(args.niftis)]
        # Otherwise, make the log in the same dir as the input file and read the list
        else:
            logfile = f"{args.niftis.with_suffix('')}_{args.command}_log.jsonl"
            with args.niftis.open() as f:
                nifti_list = [x for x in f.read().splitlines()]
        configure_logging(logfile, args.verbose)

        if args.command == "stats":
            calculate_nifti_stats(
                nifti_list,
                args.task_list,
                args.num_workers,
                args.threads,
                args.mark_complete,
                args.gaussian,
            )
        elif args.command == "update":
            update(nifti_list, args.num_workers)
        else:
            print("Unknown command")

if __name__ == "__main__":
    mircat_stats()