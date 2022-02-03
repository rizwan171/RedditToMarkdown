import praw, csv, codecs
import uuid
import os
from dotenv import load_dotenv
load_dotenv()

client_id=os.getenv('REDDIT_CLIENT_ID')
client_secret=os.getenv('REDDIT_CLIENT_SECRET')
username=os.getenv('REDDIT_USERNAME')
password=os.getenv('REDDIT_PASSWORD')

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent='Saved posts scraper by /u/' + username,
                    username=username,
                    password=password)

reddit_home_url = 'https://www.reddit.com'

saved_models = reddit.user.me().saved(limit=None) # models: Comment, Submission

csv_file_name = str(uuid.uuid4()) + '.csv'

reddit_saved_csv = codecs.open(csv_file_name, 'w', 'utf-8') # creating our csv file

# CSV writer for better formatting
saved_csv_writer = csv.writer(reddit_saved_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
saved_csv_writer.writerow(['ID', 'Name', 'Subreddit', 'Type', 'URL', 'NoSFW']) # Column names

def handle(saved_models):
    count = 1
    for model in saved_models:
        subreddit = model.subreddit # Subreddit model that the Comment/Submission belongs to
        subr_name = subreddit.display_name
        url = reddit_home_url + model.permalink

        if isinstance(model, praw.models.Submission): # if the post is a Submission
            title = model.title
            noSfw = str(model.over_18)
            model_type = "#Post"
        else: # if the post is a Comment
            title = model.submission.title
            noSfw = str(model.submission.over_18)
            model_type = "#Comment"

        saved_csv_writer.writerow([str(count), title, subr_name, model_type, url, noSfw])

        count += 1

        model.unsave()

handle(saved_models)
reddit_saved_csv.close()

print("\nCOMPLETED!")
print("Your saved posts are available in " + csv_file_name + " file.")