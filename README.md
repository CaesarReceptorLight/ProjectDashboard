# ProjectDashboard
This module provides a complete overview of the provenance of scientific experiments in CAESAR.

**Requirements**

* OMERO server. Check the guideliness to install OMERO [here](https://github.com/CaesarReceptorLight/openmicroscopy) 
* Install the third party libraries.
  * [Node.js](https://nodejs.org)

**Installation**

1.	Copy the folder 'projectdashboard' to:
```
    /home/omero/OMERO.server/lib/python/omeroweb/
```

2.	Add Project Dashboard to the known web apps
```
    /home/omero/OMERO.server/bin/omero config append omero.web.apps '"projectdashboard"'
```

3.	Add the Project Dashboard plugin to the list of right plugins
```
   /home/omero/OMERO.server/bin/omero config append omero.web.ui.center_plugins '["ProjectDashboard", "projectdashboard
/project_dashboard_init.js.html", "project_dashboard_panel"]'  
```
4. Build the project using the following commands
```

  cd /home/omero/OMERO.server/lib/python/omeroweb/projectdashboard
  
  npm install
  
  node_modules/.bin/webpack --config webpack.config.js -p (-p for production build)
  
  /home/omero/OMERO.server/bin/omero web restart  
  ```

5.  Restart the web server
```
    /home/omero/OMERO.server/bin/omero web restart
```
Publication
-----------
* [The Story of an Experiment: A Provenance-based Semantic Approach towards Research Reproducibility](http://ceur-ws.org/Vol-2275/paper2.pdf), Sheeba Samuel, Kathrin Groeneveld, Frank Taubert, Daniel Walther, Tom Kache, Teresa Langenstück, Birgitta König-Ries, H Martin Bücker, and Christoph Biskup, SWAT4LS 2018.


