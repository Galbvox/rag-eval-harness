from anthropic import Anthropic


def make_generator(client, model="claude-sonnet-4-6"):
    def generate(query, docs):
        context = "\n".join(docs)
        prompt = f"documents:\n{context}\n\nquestion: {query}"

        resp = client.messages.create(
            model=model,
            max_tokens=200,
            system="Answer using ONLY the documents provided. "
                   "If the answer is not there, say you don't know.",
            messages=[{"role": "user", "content": prompt}],
        )

        if resp.stop_reason == "max_tokens":
            raise ValueError("answer truncated")

        return resp.content[0].text

    return generate