import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Paste your eBay verification token here
# (the one you made up earlier in the eBay developer portal)
VERIFICATION_TOKEN = "ebayebayebayebayebayebayebayebay"
ENDPOINT_URL = "https://ebay-endpoint-3rr9.onrender.com/ebay"

@app.route("/ebay", methods=["GET", "POST"])
def ebay_endpoint():
    # Handle eBay's challenge request (GET)
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code")
        if challenge_code:
            # eBay requires this specific hash to verify the endpoint
            hash_input = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
            response_hash = hashlib.sha256(hash_input.encode()).hexdigest()
            return jsonify({"challengeResponse": response_hash})
    
    # Handle actual deletion notifications (POST) — we just acknowledge them
    return "", 200

if __name__ == "__main__":
    app.run()
