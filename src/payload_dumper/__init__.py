#!/usr/bin/env python3
import argparse
import os
from multiprocessing import cpu_count

from payload_dumper import http_file
from payload_dumper.dumper import Dumper

def main():
    parser = argparse.ArgumentParser(description="OTA payload dumper")
    parser.add_argument("payloadfile", help="payload file name")
    parser.add_argument(
        "--out", default="output", help="output directory (default: 'output')"
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="extract differential OTA",
    )
    parser.add_argument(
        "--old",
        default="old",
        help="directory with original images for differential OTA (default: 'old')",
    )
    parser.add_argument(
        "--partitions",
        default="",
        help="comma separated list of partitions to extract (default: extract all)",
    )
    parser.add_argument(
        "--workers",
        default=cpu_count(),
        type=int,
        help="number of workers (default: CPU count - %d)" % cpu_count(),
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="list partitions in the payload file",
    )
    parser.add_argument(
        "--metadata",
        action="store_true",
        help="extract and display metadata file from the payload",
    )
    args = parser.parse_args()

    # Check for --out directory exists
    if not os.path.exists(args.out):
        os.makedirs(args.out)

    payload_file = args.payloadfile
    if payload_file.startswith("http://") or payload_file.startswith("https://"):
        if payload_file.startswith("https://bigota.d.miui.com/"):
            payload_file = payload_file.replace("https://bigota.d.miui.com/", "https://bkt-sgp-miui-ota-update-alisgp.oss-ap-southeast-1.aliyuncs.com/")
        elif payload_file.startswith("https://hugeota.d.miui.com/"):
            payload_file = payload_file.replace("https://hugeota.d.miui.com/", "https://bkt-sgp-miui-ota-update-alisgp.oss-ap-southeast-1.aliyuncs.com/")
        elif payload_file.startswith("https://bn.d.miui.com/"):
            payload_file = payload_file.replace("https://bn.d.miui.com/", "https://bkt-sgp-miui-ota-update-alisgp.oss-ap-southeast-1.aliyuncs.com/")
        elif payload_file.startswith("https://cdnorg.d.miui.com/"):
            payload_file = payload_file.replace("https://cdnorg.d.miui.com/", "https://bkt-sgp-miui-ota-update-alisgp.oss-ap-southeast-1.aliyuncs.com/")
        payload_file = http_file.HttpFile(payload_file)
    else:
        payload_file = open(payload_file, "rb")

    dumper = Dumper(
        payload_file,
        args.out,
        diff=args.diff,
        old=args.old,
        images=args.partitions,
        workers=args.workers,
        list_partitions=args.list,
        extract_metadata=args.metadata,
    )
    dumper.run()

    if isinstance(payload_file, http_file.HttpFile):
        print("\ntotal bytes read from network:", payload_file.total_bytes)
