# mehrp

The `mehrp` package allows you to easily play the ["mehrp" heard from Boris's terminal](https://youtu.be/mIq9jFdEfZo?t=88) in the classic action film [Golden Eye](https://www.imdb.com/title/tt0113189/).

Times you might wish for your terminal to "merhp" at you include:

 * When a long process finishes.
 * When an error occurs.
 * When important input is required.
 * To dramatically notify you that you're "in".

### Try the Demo

    > pip install mehrp
    > mehrp

### Example Usage

Play a number of merhps while blocking:

    mehrp(3)
    # merhp sounds 3 times

Play mehrps during an `input()` builtin call:

    value = mehrp_until_input()
    # merhps until user input

    value = mehrp_until_input('>')
    # same as above, but with a prompt
