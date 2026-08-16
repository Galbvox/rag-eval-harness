# JUDGE_SYSTEM = ( Fails Because ignore from semantic or equivalent case
#     "You grade an answer against source documents.\n"
#     "Reply with exactly one word: PASS or FAIL.\n"
#     "PASS only if every claim in the answer is supported "
#     "by the documents AND the answer addresses the question.\n"
#     "FAIL if anything is unsupported, missing, or contradicted."
# )

JUDGE_SYSTEM = (
    "You grade an answer against source documents.\n"
    "Reply with exactly one word: PASS or FAIL.\n"
    "Judge meaning, not wording. Paraphrasing is fine. "
    "Equivalent units are fine: 21 business days and about three weeks are the same.\n"
    "PASS if the answer addresses the question and every claim "
    "follows from the documents.\n"
    "FAIL only if the answer contradicts the documents, adds facts "
    "that are not there, or does not answer the question."
)

def make_judge(client, model="claude-sonnet-4-6"):
    def judge(query, docs, answer):
        context = "\n".join(docs)
        prompt = (
            f"documents:\n{context}\n\n"
            f"question: {query}\n\n"
            f"answer:\n{answer}"
        )

        resp = client.messages.create(
            model=model,
            max_tokens=10,
            system=JUDGE_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )

        verdict = resp.content[0].text.strip().upper()

        if verdict not in ("PASS", "FAIL"):
            raise ValueError(f"unexpected verdict: {verdict!r}")

        return verdict == "PASS"

    return judge