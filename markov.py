import random


def main(*args):
    prefixes = gen_prefix(args[0])  # Get all available prefixes
    max_markov_len = args[1]  # Maximum length of the markov chain to be generated

    print(markov(prefixes, max_markov_len))  # Get and print shitty markov chain


def gen_prefix(text):
    text = text.replace('\n', ' ').split(' ')  # Replace newlines with spaces and split sentences at spaces
    words = {word: [] for word in text}  # Generate our dict of before word values with empty 'after' values

    for before, after in zip(text, text[1:]):
        words[before].append(after)

    return words


def markov(prefixes, max_markov_len):
    # Current word were on, init to a random word from the prefixes
    cur_word = list(prefixes)[random.randint(0, len(prefixes) - 1)]
    text = ""

    for i in range(0, max_markov_len):
        text += cur_word + ' '  # Add current word to text

        if not prefixes[cur_word]:  # If there is no value in the array TODO: Fix this wew
            break

        cur_word = prefixes[cur_word][random.randint(0, len(prefixes[cur_word]) - 1)]  # Get a new cur_word from our prefixes

    return text


if __name__ == '__main__':
    main("Wot the fok did ye just say 2 me m8? i dropped out of newcastle primary skool im the sickest bloke ull ever meet & ive nicked ova 300 chocolate globbernaughts frum tha corner shop. im trained in street fitin' & im the strongest foker in tha entire newcastle gym. yer nothin to me but a cheeky lil bellend w/ a fit mum & fakebling. ill waste u and smash a fokin bottle oer yer head bruv, i swer. ya think u can fokin run ya gabber at me whilst sittin on yer arse behind a lil screen? think again wanka. im callin me homeboys rite now preparin for a proper scrap. A roomble thatll make ur nan sore jus hearin about it. yer a waste bruv. me crew be all over tha place & ill beat ya to a proper fokin pulp with me fists wanka. if i aint satisfied w/ that ill borrow me m8s cricket paddle & see if that gets u the fok out o' newcastle ya daft kunt. if ye had seen this bloody fokin mess commin ye might a' kept ya gabber from runnin. but it seems yea stupid lil twat, innit? ima shite fury & ull drown in it m8. ur ina proper mess knob.", 100)
