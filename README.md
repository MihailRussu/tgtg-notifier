## TooGoodToGo Bag Availability Notifier

A very simple script that periodically checks the availability of pre-selected "bags" (comma separated list of item ids in the `TGTG_ITEM_IDS` environment variable) on TooGoodToGo, and sends a notification for each available ones, if any.

The script automatically deploys to & runs on [Scaleway's Serverless Functions](https://www.scaleway.com/en/serverless-functions/) (which has a generous free tier, so this basically costs nothing to run), deployed with GitHub Actions & [Serverless Framework](https://www.serverless.com) and mainly depends on the [tgtg](https://github.com/ahivert/tgtg-python) library.
