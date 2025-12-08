# Audio Multimodal Voice Transcription Project

The speaker discusses their ongoing work involving a voice-centric project experimenting with audio multimodal voice transcription. They are using voice to record information, which they then transcribe for evaluation and development purposes.

---

All right, so I thought I would just record, as this is a voice-centric working project and experiment that I'm working on, and these are kind of components in it.

I thought I will use voice for recording this information and then transcribe it.

You might hear some words from a little—this is my assistant. He's new to the—he's new to the project. He was doing his first podcast. His name is Ezra.

So he might just kind of jump in with some thoughts.

Audio multimodal—Ezra, do you think it's the way forward? I think it's the way forward. I think it's great because I can hold you, and I can, you know, do serious person things, like writing emails.

You don't have to do that yet. It's it must be so nice. But maybe, maybe when you're older, they'll just be, we'll just be teleporting information. The power company will send you a bill and you'll say "pay it" and it'll just zoom out.

So, getting back to the audio multimodals.

Okay, this this prompt, this repository is just some evaluation prompts. I just got VoxTro running from Mistral. And I don't want to get ahead of myself or too excited about it because it would be really great to be able to play around with this locally. There's also Quen. It's actually not a huge amount of audio multimodal models. But then you have two forms of multimodal where you can do audio understanding.

One of those is audio multimodal, which is VoxTro is probably the best example I've seen so far. And I think actually if I were to sort of bank or bet on one, or say, like, that's a good idea, I think it's a good idea to be audio specific. And for what these can offer over speech to text and traditional ASR is, I think, very significant. But I think, this is just my opinion here rather than anything else.

If you like these Omni models, it's kind of a—I think it's better to go a bit more narrow. So I'm actually very excited if I can try Vox, VoxTro. There's actually only two VoxTros that Mistral released in the summer. The only one I can run is the smaller one. There is, I think it's tiny and small.

So that's kind of good in the sense that there aren't, it's not like a massive web of quantizations out there to kind of wait through. And of course, in cloud models, there is Gemini with audio understanding etcetera. There is, the reason I'm most excited about these models is for voice transcription technology because we can do, we can add features—just going to reposition the mic a tiny bit there—we can add, basically, consolidate a single workflow for transcribe transcription and rewriting into just one into one go. So in this, the method of creating this this bank of prompts was basically trying to think of the transcription folder, the things that are most useful for me to try out. Like, how well can it actually do the transcribe and rewrite thing?

And I turned it over to two things I like using Claude for and LLMs for in terms of prompt engineering and evaluations are the, offloading the tedium of writing the prompts one by one, which was taking an eternity. And I use it for that. And then the second thing I like is, okay, here's what I'm trying to do. Here's what I've thought of so far. That would be good to evaluate: diarization, accent identification, audio quality. What do you think I'm missing? So some of, some of those ones came from Claude. So method of operation here is for anyone wanting to, exploring the space, is just use these in conjunction with a test audio file or multiple ones. The ones that I think actually would be potentially very interesting—well, actually, there's a lot of ones that are that are very potentially interesting. One is speaker obfuscation is one I hadn't actually thought of before, and speaker identification, which I've seen work with Gemini, where it's like label, label the speakers, and come up with a placeholder name. Another one that I will add, which I've also used, is providing the names. So you say, the male voice is Daniel, the female voice is something else, and then say diarize. And when this works, you've kind of got a pioneer. You know, I could say I could say the baby is, is Ezra, the man is Daniel, and we could get a transcript where the only thing is that he's not really saying words. But you know, he will be soon. And—

Lala?

Okay, so that's the, that's what's going on here.
