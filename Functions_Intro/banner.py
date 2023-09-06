def banner_text(text=" ", screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("I'm making a big banner", 60)
banner_text("Full of lovely words", 60)
banner_text(screen_width=60)
banner_text("Lovely lovely words that I hopefully spell correctly", 60)
banner_text("*", 60)
