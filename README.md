# RedditToMarkdown

Export Reddit Post and comments to a markdown format.<br>
This repo is a fork of [farnots/RedditToMarkdown](https://github.com/farnots/RedditToMarkdown) and adds 2 new scripts:

- `saved_to_md.py`
  - This script allows you to download all your saved Reddit posts as markdown.
- `selenium_script.py`
  - This script allows you to download multiple links as markdown from a text file.

Below is a screenshot of the export page built by [farnots](https://github.com/farnots):
![Example](https://raw.githubusercontent.com/farnots/RedditToMarkdown/master/exemple.png)

## Usage

### Using the export page

To view the page above:

- You can download the source and open the `index.html` file
- Or just go to [https://farnots.github.io/RedditToMarkdown/](https://farnots.github.io/RedditToMarkdown/) to try it directly from your browser

### Using the `saved_to_md.py` script to download all your saved posts

#### Prerequisites

- A Reddit account and app to use this. To setup a Reddit app and obtain the necessary client ID and secret, please follow Reddit's [First Steps documentation](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps).<br>
- Firefox browser
- GeckoDriver, which can be obtained from the [Mozilla releases page](https://github.com/mozilla/geckodriver/releases)
- Python 3

#### Setting up environment variables

The project inclues a `.env.example` file of all the environment variablesin this project. Copy this, rename it to `.env`, and set the variables without quotes. The environment variables to set are as follow:

- `REDDIT_CLIENT_ID`: Reddit app client ID. See [Prerequisites](#prerequisites) to obtain one.
- `REDDIT_CLIENT_SECRET`: Reddit app client secret. See [Prerequisites](#prerequisites) to obtain one.
- `REDDIT_USERNAME`: The username of the Reddit account you wish to download saved posts from.
- `REDDIT_PASSWORD`: The password of the Reddit account you wish to download saved posts from.
- `PATH_TO_FIREFOX_DRIVER`: Path to the geckodriver executable.
- `PATH_TO_INDEX_HTML`: Path to the `index.html` file located in the root of this project.
- `PATH_TO_FIREFOX_EXE`: Path to the Firefox browser executable.

#### Installing required dependencies

Run `pip install -r requirements.txt` in your terminal to install the required dependencies.

#### Running the script

Run the `saved_to_md.py` script in your terminal. This will download all your saved posts to markdown and place them individually in your browser downloads folder. Some settings can be changed:

- `generateTxt` (default `True`): A flag, when true, that generated a text file `links.txt.` in the root of this project with links to all saved posts.
  - Set `generateTxt` to `False` in `saved_to_md.py` to stop this happening.
- Unsaving saved posts after downloading (by default, will NOT unsave)
  - To unsave saved posts after downloading, uncommnent `# saved.unsave()` in `saved_to_md.py`

### Using `selenium_script.py`

#### Prerequisites

Please refer to [Prerequisites](#prerequisites) above.

#### Setting up environment variables

The project inclues a `.env.example` file of all the environment variablesin this project. Copy this, rename it to `.env`, and set the variables without quotes. The environment variables to set are as follow:

- `PATH_TO_FIREFOX_DRIVER`: Path to the geckodriver executable.
- `PATH_TO_OUTPUT_DIR`: Path to an output directory to save markdown files to.
- `PATH_TO_INDEX_HTML`: Path to the `index.html` file located in the root of this project.

#### Installing required dependencies

Please refer to [Installing required dependencies](#installing-required-dependencies) above.

#### Running the script

To run:

- Create a `links.txt` file in the root of this project, and paste in the links you want to download. Each link should be on a new line.
- Run the `selenium_script.py` script in your terminal. This will place the downloaded markdown files in the output directory you specified.

## Acknowledgements

Full credit goes to [Lucas Tarasconi (farnots)](https://github.com/farnots) for the markdown export and download functionality which made the selenium updates possible.
