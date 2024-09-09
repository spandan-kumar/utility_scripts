function labelEmails() {
  var sender = "specific_sender@example.com";  // Change to the sender's email
  var keywords = ["urgent", "action required"];  // List of keywords
  var labelName = "Important";  // Label to apply (must exist in Gmail)

  var threads = GmailApp.search('from:' + sender);

  for (var i = 0; i < threads.length; i++) {
    var messages = threads[i].getMessages();
    for (var j = 0; j < messages.length; j++) {
      var message = messages[j];
      var subject = message.getSubject();
      var body = message.getBody();

      for (var k = 0; k < keywords.length; k++) {
        var keyword = keywords[k];
        if (subject.toLowerCase().indexOf(keyword.toLowerCase()) !== -1 || 
            body.toLowerCase().indexOf(keyword.toLowerCase()) !== -1) {
          
          var label = GmailApp.getUserLabelByName(labelName);
          if (!label) {
            label = GmailApp.createLabel(labelName);
          }
          threads[i].addLabel(label);
          break;
        }
      }
    }
  }
}
