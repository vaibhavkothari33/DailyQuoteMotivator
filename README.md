<body>
    <div class="container">
        <h1>DailyQuoteMotivator</h1>
        <p>DailyQuoteMotivator is a Python script designed to send a daily motivational quote via email. This script fetches a random motivational quote from the Quotable API and sends it to a specified email address at a scheduled time each day.</p>
                <h2>Features</h2>
        <ul>
            <li>Fetches a random motivational quote from the Quotable API.</li>
            <li>Sends the quote via email to a specified recipient.</li>
            <li>Schedule the email to be sent daily at a specific time.</li>
            <li>Easy to configure and use.</li>
        </ul>

<h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li><code>requests</code> library (install via <code>pip install requests</code>)</li>
            <li><code>schedule</code> library (install via <code>pip install schedule</code>)</li>
        </ul>
        <h2>Installation</h2>
        <ol>
            <li>Clone the repository:</li>
            <code>git clone https://github.com/yourusername/DailyQuoteMotivator.git</code>
            <li>Navigate to the project directory:</li>
            <code>cd DailyQuoteMotivator</code>
            <li>Install the required Python libraries:</li>
            <code>pip install -r requirements.txt</code>
            <li>Update the email configuration in the script:</li>
            <ul>
                <li>Set the sender's email address (<code>from_addr</code>) to your email address.</li>
                <li>Set the recipient's email address (<code>to_addr</code>) to the desired recipient's email address.</li>
                <li>Enter your email password in the <code>server.login()</code> function call.</li>
            </ul>
        </ol>
        <h2>Usage</h2>
        <ol>
            <li>Run the script:</li>
            <code>python daily_quote_motivator.py</code>
            <li>The script will send a motivational quote to the specified email address at the scheduled time each day.</li>
        </ol>
        <h2>Customization</h2>
        <ul>
            <li>You can customize the scheduled time for sending emails by modifying the <code>schedule.every().day.at("HH:MM").do(send_daily_quote)</code> line in the script.</li>
            <li>For additional customization or modification, feel free to explore the code and make changes according to your requirements.</li>
        </ul>
      <h2>Contribution</h2>
        <p>Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.</p> 
    </div>
</body>
</html>
