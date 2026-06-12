<!-- PROJECT TITLE -->
<h1 id="toc" align="center">DietSprint<br>(Agile Software Development Project)</h1>

<!-- TABLE OF CONTENTS -->
<h2>Table of Contents</h2>
<ol>
  <li><a href="#about-the-project">About The Project</a></li>
  <ul>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#project-description">Project Description</a></li>
  </ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#overview">Overview</a></li>
</ol>


<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project">About The Project</h2>

<!-- BUILT WITH-->
<h3 id="built-with">Built With</h3>
<p>Languages : </p>

[![Python][Python.img]][Python-url]
![Html][Html.img]

<p>Development Env : </p>

[![VSCode][VSCode.img]][VSCode-url]

<p>Database : </p>

[![MongoDB][MongoDB.img]][MongoDB-url]

<p>Libraries : </p>

[![Flask][Flask.img]][Flask-url]
[![Requests][Requests.img]][Requests-url]
[![Functools][Functools.img]][Functools-url]
[![Npm][Npm.img]][Npm-url]
[![Bcrypt][Bcrypt.img]][Bcrypt-url]

<!-- PROJECT DESCRIPTION -->
<h3 id="project-description">Project Description</h2>
<h4>Project Overview</h4>
<p>
DietSprint is a lightweight, user-centric web application designed to simplify the health and weight management journey. Developed using an Agile methodology, the application rejects the bloated onboarding processes of traditional health apps, allowing users to instantly set health targets and dynamically track their progress through intuitive data visualization.
</p>

<h4>The Problem Statement</h4>
<p>
  Most diet and fitness applications on the market suffer from "onboarding fatigue." They force users through tedious, multi-step registration forms and psychological surveys before they can even view the dashboard. Furthermore, many of these apps display progress in dense, uninspiring text logs, causing users to lose motivation and abandon their goals early on.
</p>


<h4>Key Features & Scope</h4>
<ul>
  <li>Frictionless Onboarding: Zero-fuss entry. Users can skip exhausting registration forms and dive straight into the utility of the app.</li>
  <li>Target Setting Engine: A streamlined interface that helps users quickly define, adjust, and lock in their weight or nutritional targets.</li>
  <li>Visual Progress Tracker: A dynamic dashboard that transforms daily metrics into clear, motivational visual charts, letting users see their journey at a single glance.</li>
</ul>

<h4>The Competitive Advantage</h4>
<p>
  Unlike bloated competitors that require heavy data input up front, DietSprint focuses on immediate utility and visual gratification. By combining a zero-barrier entry with high-impact visual tracking, the app keeps users engaged with what matters most: their progress.
</p>

<h4>Development Approach</h4>
<p>
  Built using Agile software development, this project was executed in iterative sprints to prioritize core user value. This approach ensured that the user interface remained lean, fast, and strictly focused on solving the core pain points of goal-setting and visualization without feature creep.
</p>

<!-- FEATURES -->
<h2 id="features">Features</h2>
<p>
  The application's codebase is structured into modular subsystems designed to handle business logic, data persistence, and security verification efficiently without external bloat.
</p>

<h4>Main Routing Subsystem (<code>routes/main.py</code>)</h4>
<p>
  This module manages core application routing, view rendering, and stateful session access control. It handles traffic routing and enforces security boundaries across the platform.
</p>
<ul>
    <li>
        <strong>Access Control Middleware:</strong> Unauthorized endpoint access is blocked using custom decorators to enforce authentication policies.
        <ul>
            <li><code>@login_required</code>: Inspects the active user session. If no username is present in <code>session()</code>, the request is treated as unauthenticated and intercepted.</li>
            <li><code>@registeration_required</code>: Interrogates the database for the user's <code>register_status</code> (a boolean flag). If evaluated as <code>False</code>, the system blocks dashboard access and programmatically redirects the user back to their exact location in the multi-step registration pipeline, restoring their previously cached input data.</li>
        </ul>
    </li>
    <li><strong>Session Management:</strong> Upon successful authentication, user identifiers are bound to server-side sessions to maintain state across subsequent stateless HTTP requests.</li>
</ul>

<h4>Goal-Setting Subsystem (<code>routes/register.py</code>)</h4>
<p>
  This module drives the calculation engine and multi-stage user onboarding pipeline. It processes initial physical metrics to establish foundational health targets.
</p>
<ul>
    <li><strong>Health Metrics Engine:</strong> Processes validated data from client-side forms to calculate the user's Total Daily Energy Expenditure (TDEE) and Body Mass Index (BMI).</li>
    <li><strong>Target Optimization:</strong> Generates an algorithmic, realistic baseline target weight labeled as <code>primary_goal</code>. This serves as an evidentiary recommendation for the user, while still granting them the flexibility to manually override and input their preferred target.</li>
    <li><strong>Multi-Step State Persistence:</strong> To mitigate data loss across the multi-page registration sequence, client inputs are preserved continuously within <code>session()</code> memory buffers until the final submission step.</li>
    <li><strong>Cryptographic Data Protection:</strong> To guarantee credential security, passwords undergo cryptographic salting and hashing utilizing the <code>bcrypt</code> library prior to database serialization.</li>
</ul>

<h4>Malicious Input Control Subsystem (<code>logic/validation.py</code>)</h4>
<p>
  This dedicated validation layer serves as the application's sanitization and data-integrity barrier, processing user entries against strict structural and safety boundaries.
</p>
<ul>
    <li><strong>Input Sanitization:</strong> Intercepts incoming form data to verify data types, preventing common exploits (e.g., blocking alphabetic strings in numeric metric fields) and throwing clear exception messages.</li>
    <li>
        <strong>Biometric Boundary Validation:</strong> Enforces health-safety thresholds during input processing.
        <ul>
            <li><code>validate_primary_goal()</code>: Runs a predictive calculation on the user’s projected BMI based on their target inputs. If the calculation yields a value indicating an underweight or overweight status, the function flags the anomaly and returns a contextual error message to warn the user before the goal is committed to the system.</li>
        </ul>
    </li>
</ul>

<!-- OVERVIEW -->
<h2 id="overview">Overview</h2>


<!-- MARKDOWN & IMAGES -->
[Python.img]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[VSCode.img]: https://img.shields.io/badge/VS_code-22AEF3?style=for-the-badge
[VSCode-url]: https://code.visualstudio.com/
[MongoDB.img]: https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/
[Html.img]: https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white

[Flask.img]: https://img.shields.io/badge/Flask-3CADF3?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://flask.palletsprojects.com/en/stable/
[Requests.img]: https://img.shields.io/badge/Requests-000000?style=for-the-badge
[Requests-url]: https://pypi.org/project/requests/
[Functools.img]: https://img.shields.io/badge/Functools-000000?style=for-the-badge
[Functools-url]: https://docs.python.org/3/library/functools.html
[Npm.img]: https://img.shields.io/badge/NPM-CB3837?style=for-the-badge&logo=npm&logoColor=white
[Npm-url]: https://www.npmjs.com/
[Bcrypt.img]: https://img.shields.io/badge/Bcrypt-CB3837?style=for-the-badge
[Bcrypt-url]: https://www.npmjs.com/package/bcrypt
