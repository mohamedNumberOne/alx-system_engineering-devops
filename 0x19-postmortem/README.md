Postmortem: Web Stack Debugging Project Outage #Issue Summary Duration of the Outage:

Start: 2024-06-22 08:00 AM (UTC) End: 2024-06-22 12:00 PM (UTC) #Impact:

Service: BookShelf Browsing and Favorites User Experience: Users were unable to browse books or add them to their favorites. Affected Users: 80% of users were impacted, experiencing slow response times or complete failure to load the browsing and favorites functionalities. #Root Cause:

A misconfiguration in the Webpack development server setup caused an issue with module resolution and prevented the server from properly serving the frontend application.

When you realize the outage was due to a single line of misconfiguration.

#Timeline 08:00 AM: Issue detected via monitoring alert indicating increased error rates and slow response times. 08:05 AM: Engineering team received notification from monitoring system. 08:10 AM: Initial investigation began; assumption was a server overload due to high traffic. 08:30 AM: Checked server logs and resource usage; no signs of overload or memory issues. 09:00 AM: Focus shifted to the application code; noticed errors in Webpack configuration. 09:15 AM: Misleading path: assumed an issue with recent GSAP library update. 09:45 AM: Further investigation revealed Webpack module resolution errors. 10:00 AM: Escalated to frontend team (Abdeassamad Mourgh) for detailed Webpack inspection. 10:30 AM: Identified and confirmed misconfiguration in Webpack dev server setup. 11:00 AM: Applied configuration fix and redeployed the frontend application. 11:30 AM: Monitoring indicated resolution of errors; normal service restored. 12:00 PM: Outage officially marked as resolved after confirming stability.

#Root Cause and Resolution Root Cause:

The issue stemmed from a misconfiguration in the Webpack development server. Specifically, the alias configuration was incorrect, leading to module resolution errors. This prevented the frontend application from loading correctly, thus impacting the book browsing and favorites functionalities.

Resolution:

The Webpack configuration was corrected by ensuring the alias paths were properly defined. The following changes were made: Updated webpack.dev.js to use dynamic imports for ES modules. Corrected the alias configuration to ensure all paths resolved correctly. After making these changes, the frontend application was redeployed, restoring normal service. Corrective and Preventative Measures Improvements and Fixes:

Enhance monitoring: Improve monitoring to detect specific Webpack and module resolution errors. Documentation: Update project documentation to include detailed Webpack configuration guidelines. Training: Provide additional training for the team on Webpack configurations and common pitfalls. Tasks to Address the Issue:

Patch Webpack configuration to use dynamic imports for ES modules. Add monitoring alerts for module resolution errors. Update project documentation with Webpack configuration best practices. Conduct a team training session on Webpack and module resolution. Implement automated tests to validate Webpack configuration during the CI/CD pipeline.

#Bonus: The Outage Dance

Our servers dancing their way back to health.

By addressing these corrective and preventative measures, we aim to prevent similar issues from occurring in the future and improve the overall robustness of our development and deployment processes.
