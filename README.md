# Kaggle_Badge

<div align="center">
  <img src="https://github.com/ComputingVictor/ComputingVictor/assets/115224707/2892ab05-9f33-4146-b892-f2b6d8bd37da" width="300">
</div>

## Description
`Kaggle_Badge` is a project designed to create customizable badges showcasing Kaggle user profiles and data. It employs Selenium to scrape profile information directly from the Kaggle website and generates a badge based on a pre-defined template. This project uses GitHub Actions to automate the entire process, including setting up the Docker environment, so there's no need to have Docker installed on your local system.

## Technologies
- **GitHub Actions**: Automates the data extraction and badge generation process within a Docker container, requiring no local Docker installation.
- **Selenium**: For navigating the Kaggle page and extracting required data.

## Usage
To use this project, follow these steps:
1. Fork the repository to your own GitHub account.
2. Go to the Actions tab in your forked repository.
3. Modify the workflow file to include your Kaggle username and desired cache settings.
4. GitHub Actions will handle the rest, executing within Docker automatically, and creating a compressed image artifact of the badge.

## Contributing
`Kaggle_Badge` is an open community project. The project is in its early stages, with many areas for improvement, particularly in badge design and functionality expansion. If you have ideas or contributions, you are encouraged to participate. You can do so in the following ways:
- **Fork** the repository and clone your fork locally.
- Create a new **branch** for your changes.
- Implement your features or improvements.
- Submit a **pull request** to merge your changes back into the main project.

## License
This project is licensed under APACHE 2.0 , allowing others to use, modify, and distribute the project in various ways. Please see the `LICENSE` file for more details.

## Acknowledgments
We appreciate everyone who contributes to improving this project and look forward to building a useful tool for the community with your help.

---

### Note
This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Kaggle.com, or any of its subsidiaries or affiliates.

