from pr_review_utils import fetch_prs, post_review_comment, review_pr


def main():
    # Main function to run the bot
    # Replace with the repository you want to monitor
    repo = "offbeatlabs/covergenie"
    pull_requests = fetch_prs(repo)

    for pr in pull_requests:
        review = review_pr(pr)
        comment = post_review_comment(repo, pr, review)
        print(f"Posted review for PR #{pr['number']}: {review}")


if __name__ == "__main__":
    main()
