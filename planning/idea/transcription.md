# Speech-to-Text Project Context and Roadmap

> This voice note outlines the context, idea, and roadmap for a speech-to-text project, focusing on multimodal audio processing. The goal is to create a local, GPU-accelerated system for efficient audio transcription with cleanup features.

*Transcribed: 7 Dec 2025 14:17*

---

# Project Context and Roadmap

Okay, so the purpose of this voice recording is primarily to provide context data to the AI agent, and of course, if anyone happens to listen to this—another human—that would be cool. Hello, human. Hello, agent. I'm going to provide context data for what I'm trying to achieve in this repository, explain the idea, and provide a sort of roadmap for the plan here.

I've created a number of speech-to-text prototypes over the past year, and something I feel about speech transcription, having used it a lot, is that multimodal audio is, I think, the way forward.

Instead of providing an audio file to a speech-to-text model and then providing that transcription to a model—a large language model—for cleanup, as it were, it's much easier to just upload something to a multimodal model that has audio understanding as a capability, and can also accept a text input—in other words, a prompt. That combination is what unlocks the workflow whereby you can upload an audio file and say, give it some direction as to how to transcribe it. So, you can say, "This is an email, transcribe it as an email." But more basically, what I want to achieve here is what I call a "cleanup"—general cleanup instruction—which basically says to the model, "Transcribe this, but don't just transcribe verbatim. Add punctuation and paragraph spacing; remove filler words."

## Edge Cases

Those would be the core ones. Then there are a couple that I sometimes add to that, which is, "If you can infer any instructions or accidental dialogue."

If I'm recording a voice note like this, and then, let's say my wife pops into my office and says, "Are we still going out at five?" and I say yes, it could make that determination that that was not part of—that's not for transcription.

Or, if I say something like, "I'm going to the shop today at four—wait, I meant five," it would infer that the transcription should be, "I'm going to the store today at five," because in the course of dictating something, I've provided a sort of embedded instruction for how that audio should be processed.

The risk for those more sort of imaginative instructions that require the model to leverage some of its reasoning power is that it can go too far, and then you're into the challenge that you need a model with more reasoning, whereas in the local context it may be challenging to get anything running at all. So, for the moment, in the first version of the implementation at least, I'd like to just stick to the basics, which are filler word removal, punctuation restoration, and crucially, paragraphs—adding paragraphs. That would get me to a very good point.

## Implementation Details

In terms of what we'll actually do, firstly, let's look for candidates. There aren't actually a huge amount of these. They're relatively new, and especially in open source, so we might draw up firstly a short list of candidates. I can do some research on Hugging Face to find and identify a few.

The next thing is, you should have the hardware in your context, but to recall, the challenges that we have are 12 GB VRAM and AMD as the GPU. So I have in Docker PyTorch Rocm as an image. And I also have Ollama, but the idea here is to avoid using an LLM just to try and keep it simple. So really, instead of doing stuff like VAD—which we might add in later, but at least initially—we're just going to try and find a good model. I'd like to try a few, because I think it's going to take a bit of trial and error to find something that has viability.

## Feasibility

The other question that I have regarding feasibility—if this is feasible at all—is the context window where I find that these large models, the local models, often will really struggle. With Gemini on the cloud the other day, I was able to achieve a 45-minute transcription, so in one single turn the model was able to return an edited transcript of a 45-minute recording.

I don't think that's going to work on this hardware.

So really the idea here is to see what can be achieved. I mean, it would be brilliant if we could have—the ideal would be a GUI with record, start, stop, and transcribe buttons—very basic functionalities, microphone selection. Then when I hit transcribe, we'll send the audio binary to the multimodal model inference running locally. So that this doesn't take an eternity, we need to find something that is GPU accelerated and AMD friendly, so that it can run. If we need to, what I like doing with Docker is to create stacks using stack layering. So PyTorch Rocm is there, and then we could create a new stack that leverages that, adds in the dependencies for inference for this model, whatever this turns out to be, returns the text. And that would be basically—sort of brings it up.

Later I can look at sort of keeping that going as a persistent background service, but for the moment, for testing, let's add easy mechanisms for bringing that stack up and down. Finally, well, proof of concept first, and then we can look at the whether what we can do with it.

We should look for the context window as well and sort of think how many tokens. I'm not familiar with how audio tokenization works. So for example, this note that I'm going to be sending to Gemini for transcription—I'm looking at the timer here, it's about seven minutes, and whatever bit rate it is, I'm not sure, but how many tokens is that? Could we even fit 10 minutes in?

So as much as trying to see if it's feasible, we're also trying to probe the extent of the feasibility.

I can record a one-minute test audio sample where I'll deliberately do a lot of—like I just did there—saying "um" and pauses, so that we can send that to—as if it were just an email, a business email, let's say—and then send that to the model for validation to see if we get a decent transcription back.

I don't want an option for skipped the post-processing. Just a single one single operation: transcribe and clean it up, return that as text, copy icon—and that would be the POC.
