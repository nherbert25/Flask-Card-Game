from website import create_app

app = create_app()


if __name__ == '__main__':
    # automatically reruns the server everytime you save a change to a file
    app.run(debug=True)
