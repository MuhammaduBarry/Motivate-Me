import typer

app = typer.Typer()

@app.command()
def hello(word: str) -> None:
    print(word)



if __name__ == "__main__":
    app()