import uvicorn

import server


def main():
    app = server.create_app()
    uvicorn.run(app)


if __name__ == '__main__':
    main()
