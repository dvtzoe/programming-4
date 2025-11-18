#!/usr/bin/env bash

if [ $# -ne 2 ]; then
  exit 1
fi

week_num=$(printf "%02d" "$1")
ex_num=$(printf "%02d" "$2")

week_dir="week${week_num}"
src_file="${week_dir}/src/ex${ex_num}.py"
results_dir="${week_dir}/results"
output_file="${results_dir}/ex${ex_num}.txt"

if [ ! -f "$src_file" ]; then
  exit 1
fi

mkdir -p "$results_dir"

uv run "$src_file" > "$output_file" 2>&1

cat "$output_file"
