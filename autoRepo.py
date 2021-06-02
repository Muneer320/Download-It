from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

import os


def createRepo(uname, pswd, repoName):
    driver = webdriver.Chrome(executable_path=r'D:\\Driver\\chromedriver.exe')

    driver.get('https://github.com/new')

    username = driver.find_element_by_css_selector("input[type='text']")
    password = driver.find_element_by_css_selector("input[type='password']")

    username.clear()
    password.clear()

    username.send_keys(uname)
    password.send_keys(pswd)

    driver.find_element_by_css_selector("input[type='submit']").click()

    name = driver.find_element(By.ID, 'repository_name')
    name.clear()
    name.send_keys(repoName)

    time.sleep(2)

    if driver.find_element_by_class_name("btn-primary").is_enabled():
        driver.find_element_by_class_name("btn-primary").click()
    else:
        print('A repository with this name is already created on your account. Try with a different name.')
        return None

    print(f"\nYour repository with name {repoName.replace(' ', '-')} was created.\nYour Repo url: {driver.current_url}")

    driver.close()
    return driver.current_url


def commit(url):
    os.system("git init -b main")
    os.system("git add .")
    os.system("git rm autoRepo.py")
    os.system('git commit -m "First commit"')
    os.system(f"git remote add origin {url}")
    os.system("git push origin main")
    os.system("git rm --cached autoRepo.py")
    os.system('git commit -m "First commit"')
    os.system("git push origin main")


def main(uname, pswd):
    task = input("\n\nWhat do you want me to do?\ni) Create a repository\nii) Upload your files to the repository\niii) Both\n(Please just write 'i', 'ii' or 'iii'): ").lower()

    if task == 'i':
        repoName = input("\nName of Repository >>> ")
        createRepo(uname, pswd, repoName)

        time.sleep(3)

    elif task == 'ii':
        url = input("URL of your repo >>> ")
        work = commit(url)

        time.sleep(5)

    elif task == 'iii':
        repoName = input("Name of Repository >>> ")
        url = createRepo(uname, pswd, repoName)
        if url != None:
            work = commit(url)

        time.sleep(5)

    else:
        print("Please enter a valid input.\n")
        time.sleep(2)

        main(uname, pswd)


if __name__ == "__main__":
    print("\t\t*********Creaditentials*********")
    uname = input("GitHub username or email >>> ")
    pswd = input('GitHub Password >>> ')

    main(uname, pswd)