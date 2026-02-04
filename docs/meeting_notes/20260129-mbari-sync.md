## 2026-01-29 - MBARI Sync

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/89f1c3eb-a74d-432a-a1a6-daaa5eaa7e9b

**Voxel 51 Participants:**

- Sid Mehta
- Praveen Palem
- Azriel Nicdao

**MBARI Participants:**

- Laura Chrobak

**Meeting Notes:**

### Plugin Development

- Discussed two FiftyOne plugins for MBARI's workflow:
  - **YOLO v8 fine-tuning plugin** (Python-only version recommended for classification use case)
  - **Apply remote model plugin** for running inference and adding predictions to datasets
- Shared workflow for plugin development:
  - Test plugins locally using enterprise app (with S3 media support)
  - Use Claude Code with MCP server and skills to accelerate development
  - Deploy to production after local testing
- Timeline: Plugin development and training activities planned for end of March

### Dataset Context

- Current FiftyOne dataset: 10K labeled ROIs (~50 classes, 200×200 pixels)
- Full production scale: ~2M ROIs per deployment × 12 deployments/year = 24M total
- MBARI currently computes embeddings on internal on-prem infrastructure (sunk cost)

### GPU Compute Resources (Voxel51 Cluster)

- **Features:**
  - Zero setup for MBARI team (Voxel51 handles all infrastructure)
  - Autoscaling for delegated operations (compute visualization, similarity, plugins)
  - Point-and-click resource selection in the UI
- **Pricing Structure:**
  - Pay-as-you-go: Hourly rates by resource type with biweekly usage reports
  - Prepaid: Commit amount upfront (e.g., $5K) for discounted rates
  - Billing: Quarterly or when $50K threshold reached
- **Next Steps:**
  - Test with small subset first to estimate costs vs. internal infrastructure
  - Compare costs before committing to larger GPU usage
  - Potentially test with existing embedding models in February/March

### Contract & Administrative

- Contract auto-renews on rolling 3-month basis (1 week notice to cancel)
- Azriel to send quarter dates for transparency

### Timeline & Action Items

- **Next week:** Laura running workshop with annotators on using the plugin
- **February:** Laura out of office (traveling to Mumbai & Scotland)
  - Danelle to be point of contact during Laura's absence
  - Possible GPU testing with Danelle while Laura is away
- **March:** Plugin development and GPU testing activities
- Laura to present GPU pricing proposal to group supervisor next Wednesday

### Transcript

00:02 Praveen Palem
Good afternoon guys.

00:04 Laura Chrobak
Hi.

00:14 Sid Mehta
Hey guys. I'm just gonna be making my lunch for part. I'm sorry, I'm just like slammed with meetings, so worries. But yeah, I think AZs anyways, probably gonna be talking for the first part, right?

00:28 Praveen Palem
Yeah, That's the plan.

00:30 Sid Mehta
Got it.

00:32 Praveen Palem
Laura, you know Danelle is gonna join, right?

00:36 Laura Chrobak
I think so. Lemme ping her.

00:41 Azriel Nicdao
Is it cold in the office there or do you also just like working with a jacket?

00:46 Laura Chrobak
It's not that cold today, I think I just needed, yeah, in case there's a draft, you know?

00:55 Azriel Nicdao
Yeah, it's been funny having all these calls with the people caught up in the storm and I like, I'm like, dang, I wish I could relate, but the honest answer is that I cannot in California, so neither can you, which is good. It's true.

01:10 Laura Chrobak
Some rigid 68 degrees.

01:13 Azriel Nicdao
Sometimes Breeze gets me.

01:17 Laura Chrobak
Yeah, I'm like, oh, I think I just pinged Janelle, but I think we can start and she can hop on when she can.

01:34 Azriel Nicdao
Okay, cool. I just, Pravin, did you have any items to cover before we go into the compute stuff?

01:45 Praveen Palem
Well, well that's one of the items from last week and then there was a plugin that we discussed and then I sent you some stuff for the 51 MCP and skills. Laura, I don't know if you had a chance to like install them and try them out so we can talk about that. Why don't we start there so that we give Danelle some time because I want her to be part of the GPU cost discussion.

02:11 Laura Chrobak
Yeah, yeah, that sounds good. I don't have too much to report back unfortunately on the, on that and the plugin has been working great.

02:21 Praveen Palem
So Good.

02:24 Laura Chrobak
Sadly I don't have too much on that front to discuss.

02:28 Praveen Palem
Okay, okay, no worries. So let's, let's maybe talk about the second plugin while we wait on Danelle. Right. So for this one, there are two places we can start and I've been playing around a little bit. I, you know, there's this plugin to kind of fine tune a YOLO V eight model and apply it to, to your specific data set. And there's one purely Python version and there's one that integrates JavaScript and makes it a little more UI friendly. So there's two options to start from. I hear a lot of background.

03:18 Laura Chrobak
Oh, sorry.

03:19 Praveen Palem
Let me, Okay, cool. So I did, I did, I would say this would be a good one to like, you know, use the skills because I've been doing, I've been, I actively using the skills in the MCP server and you know, plot especially has come a long way to really do a lot of coding. So I would, we can, we can go over that a little bit, but I would highly like recommend like just taking that code and running with it and seeing how, how much you can get out of these skill sets. Is that something that's doable you think?

04:04 Laura Chrobak
Yeah, totally. I think it just hasn't hit our priority queue yet, but it's, it's right there.

04:11 Praveen Palem
Got it, got it. And, and you know, you're pretty really tech savvy, you've done Python coding for, for a lot of time, right? A lot of years. How about, how about JavaScript and TypeScript, that sort of stuff?

04:23 Laura Chrobak
I've only edited other people's codes in, in Java.

04:27 Praveen Palem
Okay. Okay. Got It.

04:28 Sid Mehta
Yeah, so yeah, I think maybe what we can do then is that we have this, like we have what the Python only one and so that's the one that does like fine tuning, but it is like an only, it is doing the object detection use case. So that would be a good one then maybe to like take and edit and maybe just change it for a classification use case as well. And then that way you can also customize it so it works on your label fields in your nomenclature. And then one thing we can do, I actually send it right now, but so when we talk about like with enterprise customers, right? We generally tell them is like the ways to out, like did you ever develop plugins when you were using the open source? Laura, I forget or not that much.

05:09 Laura Chrobak
Oh, For myself.

05:11 Sid Mehta
Got it. Yeah. Yeah. So it's, yeah, that's like one of the things that we kind of wanna recreate with the enterprise where you want to like test a plugin, there's ways to test it locally and make sure that it works like local on your laptop and then that's generally what teams wanna do before they like put it on the deployment and zip it up. So we have a way where you can bring up the enterprise app locally and it's basically, so basically it's, it'll look a lot like the open source, but it'll actually work with the S3 VAC media. It also makes it that when you run plugins, like print statements and whatnot. So I actually have the instructions handy. Let me send them to you and put it in our channel right now. But that would be one thing to like just like test out and make sure you can do. So let me, where is this? Gimme one second where this is right now. I sent it three I I sent this to like every customer, so honestly I should have it, but gimme one second Cat. Oh wait, no, I know where to look for it. Sorry. Okay, so let's see here. Okay, all right. All right, I got it. And then I'm just putting into our Slack channel. Okay, cool. Yeah, so those are basically the steps you'll need to follow that I put in the Slack channel to bring up the enterprise app locally and then that'll make it really simple then to like kind of take this plugin, run it, install it, make sure that it works locally. The one thing is is that because you guys use S3, you just wanna make sure that locally you have your AWS credential set, otherwise it won't be able to render the media images. So that's like the one thing and they'll make plugin development a lot more easier. So I think the workflow that we recommend is like, okay, let's see Laura or Danelle, one of you is like trying to build this plugin. You do it, you test it, make sure it all works, and then when it all works then you do the zip up and then you upload it to the enterprise deployment. Otherwise what happens is that you're just like making changes, zip it up and then you're trying to see if it works. I think it's much better to just do that once, right? Do the live debug, make sure everything works. But yeah, it should give you a good starting point. We'll send, I guess Pravin, if you could send the her just the one that, just the fine tuning YOLO one and then it should just be taking that code and then just like changing it for the ultra lytics instead of using the detection weights probably classification. So it shouldn't be too much. But if you have any questions, let us know and we can help.

07:58 Praveen Palem
Yeah, and also I I I wanna say like that, you know, if you, if you use cloud code, especially when you connect it to the MCP server and the skills, it goes a long way in automatically doing everything for you. Like you could literally say, okay, take this code and I want you to make a classification instead of from an object detection. And it actually does a pretty good job in, in, in, in doing everything for you.

08:26 Sid Mehta
Yeah.

08:26 Praveen Palem
Yeah, that sounds good.

08:27 Laura Chrobak
You guys have, You can send it over to me.

08:28 Sid Mehta
I What? Or any or do you have access? I know we've mentioned Claude, we have access to cloud, so that's why we big up it, but do you guys actually have access to like a Yeah, Yeah, yeah. Nice. Like an MCT thing. Okay, cool. Yeah.

08:40 Praveen Palem
Yeah. And, and last Friday if you, if you look at our chat, I, I've shared the, the skills and how to, how to like install Oh stuff.

08:49 Laura Chrobak
Oh and, but did you share the plugin that I'm working off of?

08:57 Praveen Palem
Yeah, I will send that to you. Right.

09:04 Laura Chrobak
Sweet. I don't think, I didn't see, Ooh, Janelle has a focusing emoji on her slack. I don't know what that means, but she's not at work so maybe we just, I don't think she'll, she'll join us. We can record it if she wants to hear about the GPU resources, I think she would be interested in.

09:27 Praveen Palem
Yeah, sounds good. And I did reply with the, with the starting plugin in the same thread that that sit started. Great. So yeah, with that, yeah, I'm excited to do that.

09:36 Laura Chrobak
I think that we probably like our focus next week is I'm running the workshop on with our annotators on using the plugin and then we'll re probably retrain in our own facilities and so that we can start looking at the eval metrics quickly. But then I think the next soonest thing that we'd wanna do is try training within this environment and using that plugin. So yeah. Yeah, I'm seeing that as a end of March activity.

10:14 Praveen Palem
Okay, amazing.

10:16 Sid Mehta
For the one thing that you're talking about that like is going to bring the model predictions in is we have one as well, which is also like, it's called apply remote model, but that's like the one where it's like you select a couple weights and then you select that weights and then you say like prediction field and then it'll just take your inference code, run it and populate the weight. So is that something like is this thing that you're working on, is that like gonna be inference code? Would that also be helpful to wrap out around in a plugin? Because to be honest, that's like an easier one to start, right? 'cause like that's, it might be an easier one to start I guess Pravin if you have the apply remote model one as well.

10:52 Laura Chrobak
Oh, we do want to do that. The thing is here when, when I say retrain we, I guess that would only be on the test set that we would want to apply that retrained model to. So it would be fine to do it within this.

11:19 Sid Mehta
Okay.

11:19 Laura Chrobak
Yeah. Yeah, I was just that.

11:21 Sid Mehta
So yeah, we can also send you that one, that one, that one is honestly even an easier one plugin in my opinion 'cause it's just taking infants code. So yeah, I can share my screen here real quick just to show what this one looks like. But if you go here to apply remote, like this is what this plugin looks like. And I mean our inference code is pretty simple because we're using our, where is it? We're using something from our model zoo. So it's, so it's pretty simple, but like you can come in here with your own inference code and you, you can have the users select like a an S3 file path or input their own, like wherever these model weights are stored and you can kind of build that one. So this is, so again, both options to you, but I think yeah, both would probably be, could be super helpful, right? One plugin is like adding model predictions to your data set and then the other one is actually training a model, right? And then you can, we can think about how linking to those together. So whichever one.

12:15 Laura Chrobak
Cool. Sweet.

12:16 Sid Mehta
Yeah. Yeah. So we'll put this one also in the same thing. So you have that one. So yeah, and then let us know if you have any questions.

12:26 Laura Chrobak
Great. Did we want to speak at all about the GPU resource cost?

12:36 Azriel Nicdao
Yeah, I can talk about that right now just so you have it and then since Pravin the attention is in here. Yeah, you could just snip it and then send it over to them in the slack, right?

12:46 Praveen Palem
I don't know if I can do the video, but the transcript will be there but I'll, I'll go ahead and record it anyway. Yeah, probably message Just in Google. Yeah.

12:56 Azriel Nicdao
Okay, great. So I'm gonna move this so you don't see your faces should be seeing this. We put this together, there's a also a one pager I'll send over after Laura, but the name is a work in progress, but I think it's okay Vox 51 cluster. So Pravin and S have been telling me about some of the jobs or operations you're running in 51. Makes sense. You guys are computing embeddings, this new apply, yo model plugin, all these things that require some level of compute. And part of the reason why you and your team went with the managed infrastructure like in deployment is that we handle a lot of the headaches behind the infrastructure for you. So this is kind of the next best step in making your quality of life in 51 enterprises good as possible. So you don't have to do or run embeddings externally and and things like that. So there would be zero setup from your team's end. We would handle all of the setup or maintenance. It's pretty easy in terms of our end. We would just turn it on if you would want to try it out and test it out. And some of the jobs that you just mentioned, we talked about like running in France or doing model predictions, applying YOLO model. Those are the kind of custom workloads that require some baseline level of extra hardware or compute. You might have those resources elsewhere. I guess one of that was, one of the questions I wanted to ask is is I know either Danelle had mentioned that you guys compute embeddings outside of 51. So you, you do that. How is that common for most of the things like embeddings where you have to go outside of 51 and then bring those embeddings back in?

14:44 Laura Chrobak
Yeah, our data sets are really large. So what we have in 51 is like 10,000 labels. But what we're seeing in each deployment is, you know, 2 million and there are several of, there are maybe 12 of these a year. And so we run everything on an internal resources just from, that's how we've done historically. And also it's a sunk cost to us to use those resources. However, for running on a test set or on a smaller subset, I think these GPU resources could be great if we wanted to run them on the full set and it made sense from a cost perspective, that'd be fine too. It's, it's more just what works out.

15:37 Azriel Nicdao
Got it.

15:37 Praveen Palem
Yeah. And what's good is that, go ahead Pravin, Just just so that we, we have this recorded in terms of number of images. Laura, for the 10 K labels, how many images are we talking about For the 10,000 labels?

15:53 Laura Chrobak
There's one, there's one localization per label and they're rather small. These are, it's, they're like 200 by 200 pixels, but there are just many of them. Okay.

16:08 Praveen Palem
I mean 200 by 200 is the image size. But how many images are we talking about In the 10?

16:15 Laura Chrobak
There are 10,000.

16:17 Praveen Palem
Oh, the 10,000 are images, not labels. Okay.

16:20 Laura Chrobak
They're an image with an associated label.

16:22 Praveen Palem
Right, right. But but how many unique labels are there?

16:28 Sid Mehta
Here, let's pull it up I think, I think you're saying there's 10,000 images and each image has a label, right? But then are Pravin, are you asking how many classes are there for each label?

16:38 Praveen Palem
Yeah, I mean how many unique labels are there? Right? I I I don't, I don't think there'll be 10,000 unique labels. Right.

16:44 Sid Mehta
Oh, like how many?

16:45 Laura Chrobak
So like what like classifications We currently have, I wanna say probably around 50 classes.

16:53 Praveen Palem
Okay.

16:57 Laura Chrobak
But if you go into our data set here and How many actually This many.

17:19 Praveen Palem
Okay. Yeah. Less than 50, I would say like 30 maybe.

17:25 Laura Chrobak
Yeah, we might add more too.

17:26 Praveen Palem
Okay. Okay. So 50 to be safe. And then did you mention 2 million, like we went 10,000 to 2 million potentially? Or no? Did I hear that wrong?

17:35 Laura Chrobak
Yeah, so each deployment, we have millions of these ROIs. So the how how it works is this camera takes a bunch of images while the IUV is in the water and we, we run a detector or a pipeline on board that extracts ROIs and only saves those as these small image images. And there might be 2 million per deployment. And then obviously we can't have a human go through all of those for each of the maybe 12 deployments that we have. And so instead we run this model to extract initial embeddings and look at which of those looks the most promising in terms of clustering. And then upload a subsample of that to our historical annotation databases where we then have human reviewers comb through them. And what we've managed to comb through so far is the 10,000 that you see in box of 51 right now.

18:44 Praveen Palem
Got it.

18:45 Laura Chrobak
But in the future, we'll you know, be running, doing that same process continuously.

18:52 Praveen Palem
Okay. Okay. So just to, just so that we have it potentially when you run the embeddings, we are gonna run them on the 2 million images across 12 deployments. So 2 million times 12 is the total universe, Right?

19:09 Laura Chrobak
Exactly. Oh, they're very, I mean that we have an in-house way to do that, so we really don't need to do this in VLO 51 unless it's easy and not too expensive, but yeah.

19:22 Praveen Palem
Yeah, that, that's exactly what we're trying to figure out right now is we are trying to do the math and with this the, the cost estimator, we will come up with a, a rough estimate. I mean hopefully we'll come up with apples to apples comparison of what it, what it costs for you guys to run it on your infrastructure right now and what does it cost in 50 ones boxes cluster. Right.

19:43 Laura Chrobak
Got it.

19:43 Praveen Palem
So, okay.

19:44 Azriel Nicdao
Yeah, that we have, I think That's, that's helpful context and the fact that you have been running it in-house means you have baseline costs to compare. So yeah, I guess that's why this session is really useful. Okay, so that's like a feature use case, but even if it's smaller inference runs where you might just need different resource types or different types of hardware, I feel like this use case is really useful. Yeah, we have autoscaling for the background compute, so depending on the job that you want to run or delegate, whether it's compute, similarity, compute visualization or run those plugins, it'll, the resources will kinda scale de depending on that job. So how it'll work in the, the managed deployment, I think SD mentioned to me that it's pretty like point and click. So as you would then like create a job like compute visualization, it would then give you the options once this is turned on to allocate this job on a certain type of resource. Right.

20:47 Laura Chrobak
So yeah, we walked, we, we went through that last time and it did look pretty simple.

20:52 Azriel Nicdao
Okay, cool. So in terms of pricing, think of this like a menu. So depending on the, the type of job you have, you know, the the resource type that you pick. And then if you don't really have a baseline for what resource would be best given our options, and you can ask Sid and Pravin to recommend one, but the, the model is you either pay as you go, so you would then, you know, get these resource types, pick them for the job operation and then we would send you a rate card. So you and Danelle and the Embar team would know exactly how much that job is gonna charge per hour based on the resource type that you selected. And then how you track that is you get biweekly reports for, you know, how much compute you've used or how many hours of compute and the cost associated. Right? So that's the pay as you go method. That's if like you don't wanna commit anything upfront. This is typically for teams who maybe don't have a good baseline or comparison of what their in-house compute costs are. Good thing is that you do have that baseline to kind of measure and determine what would make sense. So that's where that pay upfront a pricing structure would work to where, let's say you commit like $5,000, right? To pay upfront, then you would get these discounter rates based on these, this resource type and then you would eat at that 5,000 until it's depleted and then you would kind of transition to the pay as you go pricing.

22:21 Laura Chrobak
Cool. Is there a way to see how much of it you've incurred in the, in the website?

22:28 Azriel Nicdao
I'm not sure if it's on the app yet, but I think the bi weekly report will kind of supplement that until it's fully built out on our end.

22:39 Laura Chrobak
Right? Is there a way to like estimate how much a job will cost?

22:51 Sid Mehta
Not right now. 'cause I think it, it depends on a lot of things, right? It depends like for example, if you're talking about the, yeah, if it's like basically the biggest thing is like the number of samples, right? And then even for example, the training, it also depends on like your, your training, like which weights you want to use. Also, there's different sizes of models as well. So there is like a lot of factors. So like that's why it's like a pay as you kind of go thing, right? Where like you'll only be charged with the GPU is used, right? So even if, so yeah, a good thing would be like Make a test set.

23:20 Laura Chrobak
Yeah. See how how yeah. Much it uses for a smaller set and then extrapolate.

23:25 Sid Mehta
Yeah. So yeah, that's probably the right way to go about it. And then like, yeah, so we'd maybe start with a smaller set, make sure just it works and then move it onto more production like, like sizes and whatnot is probably what I would recommend. Yeah, I'm a, I'm a step by step person so I always like going like do the smaller thing first, Whatever.

23:41 Laura Chrobak
No, this is great. I think it's, it's a lot more amenable to us than some other structures that have it by image.

23:49 Sid Mehta
Yeah, yeah, yeah. And like also there's no, like if you don't also use it, it's not like you're being charged for it, right? So if you're not running using the GU, it's not like that. Totally.

23:59 Laura Chrobak
So this Is, it's excellent. Yeah. Yeah.

24:02 Azriel Nicdao
And the idea, the idea is that similar to how you have a baseline for costs for the workloads that you're running internally, like in-house right now, as you use the pay as you go methods and like create those test sets like Sid mentioned, then you actually have a better understanding of like, oh, okay, we're expecting to run like 10 of these jobs on these data sets in the future. So if we actually like committed like 5K or something like that, that should be enough for the rest of the year. So we would get this discounted rate and then all you do from like a contracting standpoint, we don't, we already work together, you know, we already have a contract in place, so it'd be more about just you and the team saying like, we wanna opt in and then we would send you this, I think it, we call it a rate card. So this is all early adopting early adopter pricing. We'd send you the rate card and then we would set you up in the system to get those biweekly reports and your, your billed quarterly or 50,000. So like if you hit 50,000 before the quarter, then we would bill you, but if not, then the billing or invoice process would Be $50,000. Yeah. 50, 50,000. Cool. Yeah.

25:09 Laura Chrobak
So, All right, so that sounds great. If you can just maybe send me that card, we can do some calcs on, on maybe an initial set that we would want. I I, I imagine what will happen is we'll choose a set amount of money to pre allocate for a couple of tests and see how well this works for us.

25:33 Azriel Nicdao
Okay, sounds good. And then do you want to like communicate on that through Slack and as you guys figure out like what al money you wanna allocate upfront, we could just do that through Slack and then Yeah.

25:47 Laura Chrobak
Yeah, I think that this, we've got a lot going on and I am out all of February, so I, I think that this might not really manifest until March, but I'll get the grounds laid in terms of talking to our, like the group supervisor.

26:05 Sid Mehta
Yeah. Plus also we need to like have the plugins, right? You can, you can test with the embedding that we have today, but I know the embeddings models that we have today are not the embeddings models that you guys normally use. So we could do a test with there, but I think it's better to test on a workflow that like you actually want to use, which is either the supply model to load predictions in or yeah, this training. So like I also know there's like some stuff there, but like yeah, this is as, as you can know, it's a pretty flexible plan just in general. So yeah. Yeah, we, we wanna encourage you to use it more than anything.

26:33 Laura Chrobak
So On that topic as well, since I'll be out in February and I know that our three month trial ends soon, I wanted to talk about what the options are for extending this.

26:51 Azriel Nicdao
Oh yeah, I think if you don't write a written notice and I, it sounds like you guys are going along with 51, well then it just auto renews so there's nothing that you and your team would actually have to like do To extend.

27:04 Laura Chrobak
Okay. Is that always on a rolling three month basis?

27:08 Azriel Nicdao
Yeah, so, oh, okay, cool. Sweet. Rolling three month basis and then the next, the next quarter I can send you the dates if you want, but yeah, That would be really helpful.

27:18 Laura Chrobak
Just so we have transparency, I need to kind of flag this to my boss so that he knows when those come through, so, great. That's good to know. I did in, for some reason I, I thought it was different, so Awesome.

27:31 Azriel Nicdao
Yeah, I'll send you the dates for the quarters and then like, I think it's one week notice or something like that. So just the week before that date.

27:39 Laura Chrobak
Okay.

27:40 Azriel Nicdao
For the end date then you'd have to let us know, you know.

27:46 Laura Chrobak
Cool. Sweet. Well I'm super excited to get our annotators onboarded next week and I think that's everything for now. I might not have agenda items for next week. Did, was there anything that you all had?

28:16 Praveen Palem
Is there gonna be any, anyone backing you up in February? Laura?

28:21 Laura Chrobak
Well, Danelle, so Danelle and the team will be supervising the, the folks who are using the plugin. So she would be the point of contact for then I think it would be good to sync with her. She might want to do some of those GPU tests, so it might be worth coordinating between us three if we want to like work on that while I'm gone.

28:49 Sid Mehta
Yeah.

28:50 Laura Chrobak
On her.

28:50 Sid Mehta
But do, but do you think you'll have the plugin examples that can use the GPUs ready before you go on vacation? Or will it be like after Vacation?

28:58 Azriel Nicdao
Oh no, got absolutely not, unfortunately.

29:03 Sid Mehta
Yeah.

29:03 Laura Chrobak
Yeah.

29:03 Sid Mehta
So if we do the GPO test then it could be like, again on the embeddings ones that we have, but like, I don't know how, how you feel about that. 'cause I, I, I don't want you to pay for something that, you know, you, that's just No, I would want that.

29:14 Laura Chrobak
I think it would be great for us to test some of the existing models just to see, okay. My suspicion is that they won't capture it well, but if it's on a small subset it's totally fine to run a small test. I think that we could put a couple thousand like, you know, I think we could put some money into a test thing to see, it'd be great if we, if something else worked that was already set up here.

29:39 Sid Mehta
Okay. Yeah. Rather than having to build it down. No, I think that's fair. Yeah, so we can do that then I think Yeah, if you just let us know which I guess option right easy, which, which, which one of the ones and how much to spend is. And then we can go and then let you know back to our team, let you know Okay. The dos are there for you to run and then we can, and then I would use probably compute visualization, schedule it on the do and then yeah, that's probably what I would play around with.

30:02 Azriel Nicdao
Yeah, it's effectively like a light switch. So once you tell us the committed amount, we would then invoice that and then we attract the usage from there. So yeah. Cool.

30:11 Laura Chrobak
Yeah, I will bring this back to, I'll bring the pricing and what I'm suggesting that we initially pay for with the group next Wednesday. And if Danelle wants to or has the cycles to run that test while I'm out, then that'd be awesome. But if not, we can do it in March.

30:32 Azriel Nicdao
Cool. And then if, if y'all need me to hop on to just talk about pricing live, I could do that too with the group if you want.

30:38 Laura Chrobak
Cool. I think it'll, it seems really straightforward and I'm so glad that it's not a like co-pilot pay per monthly or like a robo flow pay per image. So those both work exceptional.

30:52 Azriel Nicdao
We got you the pricing geniuses at box of 51. Thank you.

30:56 Laura Chrobak
It's Really kind of the wild west in terms of paying for GPUs, truly. Yeah, it's wild to see the credit structures.

31:04 Azriel Nicdao
I understand that there's probably a business win from making it really, really opaque with a credit structure, but they are, Yeah, we were unsure if y'all got some crazy deal because of the status of the nonprofit that y'all, y'all are like, I didn't know if like your cloud provider just gave you a bunch of credits or not.

31:21 Laura Chrobak
So Internally that is not something I know, but that's a good question I'll ask.

31:34 Sid Mehta
So I'm curious, you did say there was a sunk cost running your vettings on the million dataset Now?

31:38 Laura Chrobak
Oh, I mean we run an all on internal. On internal.

31:41 Azriel Nicdao
Oh, Oh wow.

31:42 Sid Mehta
Yeah.

31:44 Laura Chrobak
Okay.

31:44 Azriel Nicdao
Got it.

31:44 Laura Chrobak
Okay. Makes sense. Some teams do have S3 buckets that they're running on, but I wouldn't say that that is the majority of Got it. Okay.

31:53 Sid Mehta
So most of it's like on-prem servers that people have access to, So that's why Right.

31:56 Laura Chrobak
Enough people are doing it. And also honestly, I think that those, it's usually so costly to, to do that, that if you have the initial finances and resources to set it up internally, it doesn't make sense. But anyways. Anyways.

32:19 Sid Mehta
Alright, cool.

32:20 Azriel Nicdao
Okay, cool.

32:21 Laura Chrobak
Alright, I think we're good.

32:22 Sid Mehta
Awesome.

32:23 Laura Chrobak
Alright.

32:23 Praveen Palem
Yeah, I'll send out minutes and, and, and I'm, I'm guessing we won't see you for the next one month, but wherever you're going, hope you have a happy vacation.

32:33 Laura Chrobak
Enjoy You. I'm gonna Mumbai and Scotland.

32:36 Praveen Palem
Oh nice. That'd be really fun.

32:38 Azriel Nicdao
Those are two Different vibes. That's awesome.

32:40 Laura Chrobak
Wow. I know I, the packing for this trip is insane.

32:44 Sid Mehta
Yeah. Wait, where's Colin?

32:45 Laura Chrobak
Are you going? Edinburgh? There's a ocean science meeting in Glasgow. Okay. So we'll be there. And then I have a friend who's getting married in Pune, so.

32:58 Sid Mehta
Okay. Yeah. Yeah, that'll be fun. Yeah. Well I'm going to Edinburgh 'cause my sister-in-law's studying abroad there, so we're gonna visit her in April, so.

33:06 Laura Chrobak
Oh, fun. That's Why I was asking. Yeah, yeah, yeah.

33:08 Sid Mehta
And I was also just in India, so Yeah. Yes. Yeah, Yeah.

33:11 Laura Chrobak
Edinburgh is so cool. April will still be pretty chilly, but we're going to the botanical gardens, which I hear are some of the most incredible ones.

33:20 Sid Mehta
Oh, okay.

33:21 Laura Chrobak
In the uk. And I'm going to a pickle shop that I've been wanting to go to for many, many years. So if either of them turn out to be good, I will let you know so that you can then also go Yeah, yeah. Pickle shop.

33:35 Sid Mehta
I love it.

33:35 Azriel Nicdao
I taste my shots with pickle juice, so maybe you're like best friends.

33:39 Laura Chrobak
I know. Fair enough. Yeah, this place that has all sorts of pickled goods and then you can eat it. But I will follow up on the DPU pricing and I think you guys should coordinate with Janelle about meetings. I won't be at the one next week and we'll just let the next three months roll through because that's easy and great.

34:03 Praveen Palem
Nice.

34:04 Laura Chrobak
Cool.

34:05 Praveen Palem
Alright everyone.

34:06 Laura Chrobak
Yeah.

34:07 Praveen Palem
Bye bye. Safe travels. Thank You.
