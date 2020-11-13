######################################
import tweepy

consumer_key = 'OCfCwmv3FroihdCa5242JkUO7'
consumer_secret = 'hPgCKNl2J5BjrUxkCaCFqIjmFlE63iT3dhe1oTjHeVb97vDojx'
access_token = '222342647-D7chKQaPFtGB51U775EWPfQtN4Gt9TRafGUaaRST'
access_token_secret = 'q2X36IL9LR988RzcQ7aiWQrDmFpeGImvSjZmpMACwMIYJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file_test = open("test.txt", "w", encoding="utf8" )

for tweet in tweepy.Cursor(api.search, q="bún chả", result_type="recent", lang="vi", tweet_mode='extended').items(100):
    file_test.write(tweet.full_text)

file_test.close()


######################################

file_train_non_spam = open("train-nonspam.txt", "r", encoding="utf8")
all_tweets_non_spam = file_train_non_spam.read()

with open('train-nonspam.txt', "r", encoding="utf8") as myfile:
    num_train_non_spam = sum(1 for line in myfile if line.rstrip('\n'))

file_train_non_spam.close()
all_word_non_spam = all_tweets_non_spam.replace("\n", ' ')
list_word_non_spam = all_tweets_non_spam.split();
num_word_non_spam = len(list_word_non_spam)


######################################

file_train_spam = open("train-spam.txt", "r", encoding="utf8")
all_tweets_spam = file_train_spam.read()

with open('train-spam.txt', "r", encoding="utf8") as myfile:
    num_train_spam = sum(1 for line in myfile if line.rstrip('\n'))

file_train_spam.close()
all_word_spam = all_tweets_spam.replace("\n", ' ')
list_word_spam = all_word_spam.split();
num_word_spam = len(list_word_spam)


######################################
all_word = all_word_non_spam + " " + all_word_spam
list_word = all_word.split()
list_word = set(list_word)
list_word = list(list_word)
list_word.sort()

count_word = len(list_word)

######################################

f_non_spam = [];
ifns = 0
while ifns < count_word:
	f_non_spam.append(0)
	ifns += 1

for num in range(count_word):
	for i in range(num_word_non_spam):
		if(list_word[num] == list_word_non_spam[i]):
			f_non_spam[num] = f_non_spam[num] + 1;


#######################################

f_spam = [0];
ifs = 0
while ifs < count_word:
	f_spam.append(0)
	ifs += 1

for num in range(count_word):
	for i in range(num_word_spam):
		if(list_word[num] == list_word_spam[i]):
			f_spam[num] = f_spam[num] + 1;


######################################
list_test = []
with open("test.txt", "r", encoding="utf8") as file_test:
    for l in file_test:
        list_test.append(l.strip())


###################################### Test
#for x in range(len(list_test)):
	# lt = list_test[x]



lt = list_test[0]

list_word_test = lt.split()
num_word_test = len(list_word_test)
f_test = []


ift = 0;
while ift < count_word:
	f_test.append(0)
	ift += 1


for num in range(count_word):
	for i in range(0, num_word_test	 - 1):
		if(list_word[num] == list_word_test[i]):
			f_test[num] = f_test[num] + 1;



lt_ns = num_train_non_spam/(num_train_non_spam + num_train_spam)
lt_s  = num_train_spam/(num_train_non_spam + num_train_spam)


for num in range(count_word):
	if(f_test[num] == 0):
		continue
	elif f_test[num] > 0:
		tsns = f_non_spam[num] + 1
		ms = num_word_non_spam + count_word
		lt_ns *= pow((tsns/ms),f_test[num])

		tss = f_spam[num] + 1
		lt_s *= pow((tss/ms), f_test[num])
	

P_non_spam = (lt_ns)/(lt_ns + lt_s)
P_spam = (lt_s)/(lt_ns + lt_s)

print("tweets: " + lt)
print("non spam: ")
print(P_non_spam)
print("spam: ")
print(P_spam)

if P_non_spam >= P_spam:
	print("===> Non Spam")
elif P_non_spam < P_spam:
	print("===> Spam")




