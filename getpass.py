{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOwoyb2r706zrGu4nraLEjZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ponrudee/Langchain/blob/main/getpass_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XSj8RCWnfvND"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "\n",
        "def get_api_key():\n",
        "    api_key = os.environ.get(\"GPT3_API_KEY\")\n",
        "    if not api_key:\n",
        "        raise ValueError(\"GPT3_API_KEY environment variable is not set.\")\n",
        "    return api_key\n",
        "\n",
        "def main():\n",
        "    api_key = get_api_key()\n",
        "    print(f\"Retrieved API key: {api_key}\")\n",
        "    # You can use the api_key for making API requests\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}
