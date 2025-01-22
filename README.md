# Template for Research and Development

# First

```
pip install -r requirements.txt
```


# Research(PoC)

```
bash scripts/test.sh
```

# Development(Service)

```
git clone this_repo

docker build -f your_path/dockerfile -t image_name .

docker run -d -p port:port --name container_name image_name

rm -rf your_path

```