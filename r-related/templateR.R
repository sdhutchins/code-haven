library("template")

# Name the package
rpackage <- "sdhtestpkg"

# Create the new project
new_project(rpackage, github = FALSE, private.repo = TRUE, travis = TRUE)

# Use a github key to authenticate
use_github(auth_token = "", pkg = rpackage, protocol = "https")
