const http = new XMLHttpRequest()
var data
var output = ''
var style = 0
var escapeNewLine = false
var spaceComment = false
var title = ''

function fetchData(url) {
  output = ''

  http.open("GET", `${url}.json`)
  http.responseType = 'json';
  http.send()

  http.onload = function() {
    data = http.response;
    const post = data[0].data.children[0].data
    let subreddit = post.subreddit_name_prefixed.replace("r/", "")
    const comments = data[1].data.children
    displayTitle(post)
    output += "\n\n## Comments\n\n"
    comments.forEach(displayComment);

    console.log("Done")
    var ouput_display = document.getElementById("ouput-display");
    var ouput_block = document.getElementById("ouput-block");
    ouput_block.removeAttribute("hidden");
    ouput_display.innerHTML = output;
    download(output, `${subreddit}.${title}.md`, 'text/plain')
  }
}

function setStyle() {
  if (document.getElementById("treeOption").checked) {
    style = 0
  } else {
    style = 1
  }

  if (document.getElementById("escapeNewLine").checked) {
    escapeNewLine = true
  } else {
    escapeNewLine = false
  }

  if (document.getElementById("spaceComment").checked) {
    spaceComment = true
  } else {
    spaceComment = false
  }
}

function startExport() {
  console.log("Start exporting")
  setStyle()

  var url = document.getElementById('url').value
  if (url) {
    fetchData(url)
  } else {
    console.log("No url provided")
  }
}

function download(text, name, type) {
  var a = document.getElementById("a");
  a.removeAttribute("disabled");
  var file = new Blob([text], {type: type});
  a.href = URL.createObjectURL(file);
  a.download = name;
}

function displayTitle(post) {
  output += `# ${post.title}\n`
  title = post.title.replace(/[\/\\#,+()$~%.'":*?<>{}]/g, '')
  
  if (post.selftext) {
    output += `\n${post.selftext}\n`
  } else {
    output += `\n${post.url}\n`
    output += `\n${post.url_overridden_by_dest}\n`
  }
  output += `\n[permalink](http://reddit.com${post.permalink})`
  output += `\nby *${post.author}* (↑ ${post.ups}/ ↓ ${post.downs})`
}

function formatComment(text) {
  if (escapeNewLine) {
    return text.replace(/(\r\n|\n|\r)/gm, "");
  } else {
    return text
  }
}

function displayComment(comment, index) {

  if (style == 0 ) {
      depthTag = '─'.repeat(comment.data.depth)
      if (depthTag != '') {
        output += `├${depthTag} `
      } else {
        output += `##### `
      }
  } else {
      depthTag = '\t'.repeat(comment.data.depth)
      if (depthTag != '') {
        output += `${depthTag}- `
      } else {
        output += `- `
      }
  }

  if (comment.data.body) {
    console.log(formatComment(comment.data.body))
    output += `${formatComment(comment.data.body)} ⏤ by *${comment.data.author}* (↑ ${comment.data.ups}/ ↓ ${comment.data.downs})\n`
  } else {
    output += 'deleted \n'
  }

  if (comment.data.replies) {
    const subComment = comment.data.replies.data.children
    subComment.forEach(displayComment)
  }

  if (comment.data.depth == 0 && comment.data.replies) {
    if (style == 0 ) {
      output += '└────\n\n'
    } 
    if (spaceComment) {
      output += '\n'
    }
  }
}
