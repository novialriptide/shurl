# Building the Model

This is being written while there is no machine-learning code available, information is subject to change.

## Fetching the Training Data

> [!IMPORTANT]
> You need to be authorized to access such Rutgers University services.

1. Make sure you are connected to Rutgers University's WiFi or VPN and is authorized to access the university's servers
2. SSH into the server, you can find instructions for this by looking at the Shrunk's wiki page
3. You can use [croc](https://github.com/schollz/croc) to transfer files from the Rutgers University servers to your local machine
4. Run this command to receive the BSON file on your machine

```
croc dump/shrunk/urls.bson
```

5. Move `urls.bson` to the `data/` directory
