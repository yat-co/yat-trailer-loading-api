# YAT Trailer Loading API

This is a sample implementation of an API hosting the services in the `yat-trailer-loading` package available on [PyPi - YTL](https://pypi.org/project/ytl/).  There are two implementation options, one using Docker and you can run directly on your machine.  There is a publicly hosted version of this API hosted on [YAT Demo](https://demo.yat.ai) with documentation here [Postman](https://documenter.getpostman.com/view/13715234/2s8ZDVZ3rH).

To read more about the trailer load optimization, see the README file in [PyPi - YTL](https://pypi.org/project/ytl/) and the references therein.  To try out the API, the best way to get started is working from the documentation [Postman](https://documenter.getpostman.com/view/13715234/2s8ZDVZ3rH) as a guide.

# Setup

To build your own trailer loading API micro-service, complete the following.

## Environment File

Using the `.env.sample` file as a template, create a `.env` file in the root directory of this project (the same directory as the `.env.sample` file).  To start, you can just copy-paste the values from `.env.sample` to `.env`.

## Hosting with Docker

Run the following from the root directory of this project.
```
docker-compose -f docker-compose.yaml build --no-cache && docker-compose -f docker-compose.yaml up

echo detached
docker-compose -f docker-compose.yaml build --no-cache && docker-compose -f docker-compose.yaml up -d
```

The API can then be accessed using the url `http://localhost`.

## Hosting Directly on Your Machine

Install requirements in `requirements.txt`, and run the following from the root directory of this project.
```
python main.py
```

The API cn then be accessed using the url `http://localhost:5000`.
