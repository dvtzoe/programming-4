#!/usr/bin/env bash

if [ $# -ne 2 ]; then
  exit 1
fi

week_dir="${1%/*}"
src_file="${week_dir}/src/$2.py"
results_dir="${week_dir}/results"
output_file="${results_dir}/$2.txt"

if [ ! -f "$src_file" ]; then
  exit 1
fi

mkdir -p "$results_dir"

cd "$week_dir" || exit 1

uv sync

cd ..

uv run "$src_file" > "$output_file" 2>&1

cat "$output_file"

cat "$output_file" | wl-copy
