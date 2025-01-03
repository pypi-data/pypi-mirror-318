export ENV_STATE=$1
export VERSION=$2

# run shell script command example
# anaconda_upload.sh prod 1.6.0

echo "ENV_STATE=$ENV_STATE"$'\n'"VERSION=$VERSION" > prismstudio/_common/config.env
echo "$VERSION" > VERSION
product_name=""
if [ "prod" == "$ENV_STATE" ]; then
    product_name="\"prismstudio\""
elif [ "stg" == "$ENV_STATE" ]; then
    product_name="\"prismstudio-stg\""
elif [ "dev" == "$ENV_STATE" ]; then
    product_name="\"prismstudio-dev\""
fi

# OS에 따라 적합한 sed 명령어 사용
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s|^name =.*|name = $product_name|" pyproject.toml # macOS
else
    sed -i "s|^name =.*|name = $product_name|" pyproject.toml     # Linux & Windows
fi

python -m build

#rm dist/*.tar.gz

#token="pypi-AgEIcHlwaS5vcmcCJGYwOGE3YmU4LWJiNDktNDA2Ny1iNWIxLWQ2NTljYTY4MmFiZQACKlszLCI0MmU2MTAyNy04MGI2LTRmOTItOGQyNy1lODAyNjZhMzQxYjciXQAABiCMx6HSUdoD3cqW4qjiObWF9YoNs-b5mprKoOWRKupYhQ"
#twine upload dist/prismstudio-* -u __token__ -p $token