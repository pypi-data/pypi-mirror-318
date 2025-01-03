export ENV_STATE=$1
export VERSION=$2

# run shell script command example
# anaconda_upload.sh prod 1.6.0

PS_FILES="/home/prism/miniconda3/envs/venv2/conda-bld/linux-64/prismstudio-*" # 빌드하는 PC와 conda 환경에 따른 경로 체크 필요
rm $PS_FILES
conda activate venv2
conda build conda-receipe --no-test
for f in $PS_FILES
do
    echo "Processing $f file..."
    conda convert -f --platform all $f -o dist/
done

ARCH=( "win-64" "osx-arm64" "linux-aarch64" )
for ar in "${ARCH[@]}"
do
    FILES="dist/$ar/*"
    for f in $FILES
    do
        echo "Uploading $f ..."
        anaconda upload $f
    done
done