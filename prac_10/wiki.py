import wikipedia

print("Wikipedia Search Tool")

while True:
    title = input("Enter page title: ").strip()
    if title == "":
        print("Thank you.")
        break

    try:
        # Correct parameter name is auto_suggest
        page = wikipedia.page(title, auto_suggest=False)

        print(page.title)
        print(page.summary[:500] + "...")
        print(page.url)

    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except wikipedia.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')

    except Exception as e:
        print("An unexpected error occurred:", e)
