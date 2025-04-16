# win: ./tree.exe -I "venv|*pycache*|hls|print_tree.sh|instance|test|tree.exe|README.md|requirements.txt" -A --dirsfirst
# linux: tree -I "*pycache*|*init*|tree.exe|instance|README.md|requirements.txt" --dirsfirst
 tree -I "app.db|venv|*pycache*|*init*|tree.exe|instance|hls|static|README.md|requirements.txt|*.wav|static" --dirsfirst
#./tree.exe -I "app.db|venv|*pycache*|hls|print_tree.sh|instance|test|tree.exe|README.md|requirements.txt|*.wav|static" -A --dirsfirst