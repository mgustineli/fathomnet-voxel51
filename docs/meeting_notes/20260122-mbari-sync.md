## 2026-01-22 - MBARI Sync

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/5b17f8ff-04b0-47a3-b9c5-ca9835071f0c

**Voxel 51 Participants:**

- Sid Mehta
- Praveen Palem

**MBARI Participants:**

- Laura Chrobak
- Danelle Cline

**Meeting Notes:**

- Demonstrated model evaluation features: precision/recall/F1 metrics, interactive confusion matrices, class-level performance analysis
- Showed scenario analysis for comparing model performance across subsets (collections, seasons, depth, etc.)
- Covered comparing multiple models side-by-side with eval runs
- Emphasized scheduling eval runs as delegated operations (background processing on DO)
- Discussed GPU compute options: pay-as-you-go pricing for custom model inference, embeddings, and fine-tuning
- Introduced YOLO v8 trainer plugin (apply model + fine-tune capabilities) - needs adaptation for classification vs detection
- Team open to using YOLO v8 architecture if it simplifies workflow (problem is data-limited not architecture-limited)
- Discussed model lineage/traceability: tracking training data state, storing metrics, referencing snapshots
- Planned workflow priorities: (1) label review/refinement, (2) model eval on ground truth, (3) model training within FiftyOne
- Next steps: get GPU pricing from AZ, decide between custom embeddings plugin vs fine-tuning plugin priority, complete first iteration before Laura's February travel

### Transcript

00:48 Sid Mehta
Hey. Hey, how are you?

00:52 Praveen Palem
Hey. Not too bad.

00:54 Sid Mehta
Oh yeah, I shouldn't have passed that. I guess I should know how you're feeling, but yeah, I hope you feel better.

00:59 Praveen Palem
Yeah, I'm just on like DayQuil so surviving on medicines right now. It's all good.

01:06 Sid Mehta
Is there an abrupt change of season or has it been snowing yet in Texas?

01:09 Praveen Palem
I feel like it's Snow guys. It's expected to snow. Snow. This weekend we, we got a winter storm coming up.

01:15 Sid Mehta
Ah, okay.

01:16 Praveen Palem
Yeah.

01:17 Sid Mehta
Yeah.

01:17 Praveen Palem
You guys are spared. It's, it's from Texas through the Carolinas.

01:21 Sid Mehta
Yeah. Yeah, I know. If it ever snows here, that means that's when you know like hell is on like we're, we're on hell on earth If it ever snows in Arizona, it never happened. But yeah, my cousins live in Dallas and like I, I remembered it snowing one weekend right before they were actually gonna come here.

01:36 Laura Chrobak
So. Hey Laura. Hey, how's it going?

01:41 Sid Mehta
Good, good.

01:42 Laura Chrobak
How are you? Pretty good. This is really zoomed in. I don't know why. Yeah, January is always a hard month. It's always smaller than it needs to be.

02:08 Sid Mehta
Oh really? Yeah, it's weird. I feel like last week was probably one of the busiest weeks I've ever had and I'm like so scared. These decisions the start of the year, right? Where normally things are generally a bit more quiet, take a while to up.

02:20 Laura Chrobak
Oh, okay.

02:21 Sid Mehta
Not the case here.

02:23 Laura Chrobak
Yeah, I feel like it's very busy here too, but I guess I think that January are typically like that. Hey, how are you At like 2 33 today? But if we're done by then that's okay. Yeah, I Can hear well can you hear us?

02:55 Danelle Cline
I can hear you.

02:56 Sid Mehta
Hey Guys.

02:57 Praveen Palem
Hey I'm, I'm going through a cold so I'll mostly be in the background.

03:02 Laura Chrobak
Okay. Better.

03:04 Praveen Palem
Yeah. Yeah, Sid lead this meeting, but I'll be taking notes and Great.

03:12 Laura Chrobak
I think we have a relatively small agenda for today because everything, we're just taking off our review and I think that we have everything that we need with the plugin right now. So I think that preemptively we had discussed maybe looking at some eval metrics for later on.

03:37 Sid Mehta
Yeah. And I can show that and what that just looks like, just how you can be able to run it and what the requirements are for you to run it. So yeah, maybe that could be helpful and then you can let us know if there's anything else. But yeah, we're happy to call a meeting short also, like I know we have like an hour standing, but normally right, sometimes we can also make it 30, 45 minutes if we feel like that's a good time going forward. 'cause I know an hour's a lot once and then you know, eventually biweekly and whatnot. But anyways, yeah, so for model eval, yeah it's like it's already there. The platform, all you have to do is just come to model evaluation and then what you'll get here is that you'll get this evaluate model to run an eval run and then you need two requirements. Well yeah, you basically, these are the requirements to basically run a model eval run. And that's to find a a, a label field that represents your model predictions. So here it might be like the first model and then you need a label field that represents your ground truth. Then you'll need provided some eval key, so like eval test and then you can, we have a dump a bunch of eval methods to use like coco open images and then you can have all this other type of configurations as well. You can also compute map as well.

04:51 Laura Chrobak
What's the Key?

04:53 Sid Mehta
The key is just, so it's like a run, right? You're at running an evaluation run. So it's to note that this is the eval run. So it's to kind of denote that this is like the point in time where you ran this eval run, right? Because what if like maybe you change the model predictions or like anything like that, right? So that's why like eval runs we, and you can also compare eval runs as well. So that's, it's basically just to give it a A name. Yeah, yeah. Whatever works for you, right? So it can be like, you know, LO test one or lo lower eval one or whatever name can convention you wanna do, you can also decide to compute like metrics like map or something like that. And yeah, there's a bunch of other like configs that you can choose here. And then the result of that eval run is something like this, right? So you have this model evaluation, we call it like a panel and it will tell you the a all the metrics that you guys that you know are pretty standard, right? So I precision recall F1 score and then if I selected a calculate map, it's just a longer thing. So you know it's, it's kind of optional and it tells you like how many true positives, false negative, false positives, false negatives, all this stuff. You can also see metric performance here. And then also you can see performance by class. So if you want to see something like what does my F1 score look like across like certain classes, that's helpful. And it's also like interactive. So if I click on this, it will then like show me all the samples in my grid that have this class. And then also confusion matrix as well, which is like interactive. So that's like another way where if I click here I can find which ones are like the false positives and false negatives. That's very nice. So pretty interactive. Yeah. And then also scenario analysis as well. I think maybe we've gone over this at some point, but it's basically a way for you to also create like model performance across subsets, right? So in this example, right, we can, we have one A scenario which is like we, we have a class, yeah, we have a field on our data set, which is the time of day. So I can see does my model perform better in time, daytime, nighttime. So, and you can define these scenarios however you want. So you might have something.

07:06 Laura Chrobak
Yeah, yeah. So could, could you show us how you did, how you might go through to define the scenario?

07:12 Sid Mehta
Yeah, so what it'll do is that let's say test mari, all right? And then, so it's the scenario type, it can depend on a lot of things, right? It can be like on a sample field, it can be on some saved views that you have attribute custom code. So we kind of make or like, you know, whatever, however you want to like, you know, yeah, define that scenario. Either you can use, like you can use it based on fields that already exist on your dataset and use those to create the subsets. Or it can be like something manual where you have like a bunch of saved views that already represents subsets of your data. So like let's say if it's select a sample field and I would select a sample field that I would wanna do this. So I think I have, yeah, time of day. We have some other interesting ones where like for example, it's like weather, right? So rainy weather or whatnot, right? That's something like a lot of our AV customers use where they have like something like rainy, snowy or whatnot. So you can see like, does my model perform good on snowy images, whatnot for you, I don't know if you take like the location or the, or like where if that's like a consideration of where these images are coming from Depth or honestly for us what's a little more interesting is we'll probably have to now the collection in some field, right? Yeah.

08:29 Laura Chrobak
And we just wanna compare and contrast different collections. So that would be a field and then it just search. So here, yeah, but if I selected that specific field, will it just automatically differentiate all of the sense vari of that? Yeah.

08:45 Sid Mehta
Yeah. It should take, I guess how many collect like distinct collections on there, right? Like do, is it like a like 10 Right now?

08:51 Laura Chrobak
Like three. But there might be more. Okay.

08:53 Sid Mehta
Yeah, yeah, yeah. So what I would expect to see is that when you choose the collection field name, that it would show you your three collections here and then you would select those and then those would be your like three scenarios that you're, that you've selected.

09:05 Danelle Cline
It could, it could be we could have season.

09:09 Sid Mehta
Yeah. Yeah, that's a good one too. Yeah, there's only four seasons, right?

09:11 Danelle Cline
So it's like, which, Yeah, we often see changes based on the season and it's, it's at that granular, it's not anymore, it's not month, it's, it's just, Yeah.

09:22 Sid Mehta
Perfect. Yeah, those all sound like exactly what the, what this was for. So that's how you define these scenarios. And then, yeah, one thing I forgot to mention is that, yeah, just like with, oh, and then you can also compare models, right? So like we did E, so this was like eval first, right? And that what it was is that it was taking one ground truth with model, like let's say model prediction from model A, right? So you could also have another eval run that has ground truth, but then model predictions from model B and then you can compare those as well. So we can see like eval. So if you see over here we have the ability to select two eval runs and kind of compare them with each other, right? So we have EV eval best eval and eval first. So yeah, imagine this was like a model A model B eval run and then you can kind of see which one's better as well. And then you should also be able to compare little Symbols.

10:13 Danelle Cline
That's Cute.

10:14 Sid Mehta
Yeah. Lets you know which one's the best. And then you can also do scenario analysis comparison as well. So you can see how like the different models also will perform differently on the different scenarios that you've defined here.

10:25 Danelle Cline
Yeah.

10:25 Sid Mehta
So, and then the only other thing was that when I was creating this eval run, I would just always, as with everything, this is gonna be a change in the tool, but like I, I know we went through this pain, Laura, where A IPD would be to just make sure you schedule this operation in the background. 'cause it can take a while. Sorry, it didn't look my eval key.

10:44 Laura Chrobak
Oh yeah. Can you tell me how to do that again?

10:47 Sid Mehta
Yeah, yeah, yeah. So this will be changing relatively soon. Like so where the default won't be execute, it'll be what the product wants you to do, which is schedule it 'cause you guys do have do set up, but it's basically right now you come down to the carrot and then you would say schedule on teams do Okay. Yeah.

11:07 Laura Chrobak
Is there a way to cancel that? If you can you stop or run If you ac?

11:13 Sid Mehta
Yeah. So if you accidentally hit execute, that's a good question. It usually just times out on its own. I think it, it only will all I, I think anyways, the product might only allow you to like execute like a a something for a certain time and if it doesn't, it'll just time out. So yeah, we're really trying to change the behavior where it just, the default is schedule. So like users don't get confused and it'll just run in the background and then you'll see it on the runs page here.

11:37 Laura Chrobak
I see. So if it fails or like if it finishes, I can see on the runs page.

11:42 Danelle Cline
Great.

11:43 Sid Mehta
Yeah, if, if you schedule it for sure if you hit the execute then it's not gonna be a delegated run, right? 'cause you, it was like an instant run. So yeah, I think that's the, so that's the caveat, but it's, if you accidentally hit execute, it's not the end of the world. It just might not run. It just might not finish. 'cause I think we do have a timeout for like in-app execution.

12:02 Laura Chrobak
'cause otherwise the app holds, Can you go back to that previous page? I was curious about this. I don't even know the words. So if you just go into one of them, That was probably the worst one to go to. But It's okay. It's just the future that I'm curious about the scenario analysis again.

12:26 Sid Mehta
Yeah.

12:28 Danelle Cline
Okay.

12:28 Laura Chrobak
This is what we just talked about it. This is where you define the scenario.

12:32 Sid Mehta
Yeah, yeah, yeah. So that's like an overview, like your overall eval run and then like after you, the eval runs completed, right? You would come in and define these scenarios based on the eval run and then it, it, yeah. So you do the eval run first, you come back, you see the overview and then you come in and define these scenarios.

12:51 Laura Chrobak
Cool. I can't wait to do this.

12:54 Danelle Cline
That sounds So, so there's a little bit of thought up front though about making sure we have everything. Yeah, the main thing is like just load Labeled and loaded the way it needs to be to do this analysis.

13:08 Sid Mehta
So yeah, which is basically the rubric requirement for this is that you need two label field in 51 at the same type, right? So you're working classification labels, right? In 51 and hopefully you have one set of labels that represents like a ground truth like we see here. And then you have like another label field that represents your model predictions and then that's how you can kind of do this analysis. Cool.

13:30 Danelle Cline
So each model, lemme stay with that for a little bit.

13:33 Laura Chrobak
Yeah, sorry.

13:35 Danelle Cline
So in your screen here, first model best model, drop that down again. Best model. Okay.

13:47 Sid Mehta
Yeah, so it's like a, so you can think of like the, right now I would say the best way a model is represented in 51 is through the label field, right? Because it, that's how you show model predictions, right? Is that it's a, it's a label right now it's kind of on the, I think end users to define like which labels are ground truth and which labels, like which label fields are ground truth fields and which ones are model prediction fields.

14:11 Danelle Cline
Is this an, is this structure in, is there sort of an enforced structure of the way this data looks for it to work?

14:17 Sid Mehta
Like Id, Oh the model. Sorry, say that again. Like what, what structure exactly?

14:29 Danelle Cline
I Guess I'm trying to understand if we run our model here, what needs to be loaded exactly.

14:34 Sid Mehta
Yeah, I think, yeah, so that's good, right? Like I think in good naming convention, basically all you need is the model. Like from the models, right? You're gonna be running inference on the samples and then you're gonna want to give in a classification label, right? So that's basically it. Okay. Now what, what is probably good to align internally is like what should be the naming convention of this label field to represent that It's a model, right? So like this is like I got a model. Yeah, yeah. So that, and that can be done in the label field name, right? So you see this is like YOLO and review. We know this is our YOLO model.

15:07 Danelle Cline
Yeah, I get it, I get it. I It's just as long as it's that type of object Classification.

15:12 Sid Mehta
Yeah, yeah, yeah, yeah. So notice how both of these are the same type. So for your, for yours, we would want both of them to be classification types.

15:18 Danelle Cline
Yes, yes.

15:20 Sid Mehta
Yeah.

15:20 Danelle Cline
Okay. Yeah, I'm, I'm remembering a cobwebs clearing. Yeah.

15:23 Sid Mehta
Yeah. Okay, cool. But yeah, did that make sense? Does that give you good overview of kind of the out of the box model evaluation functionality we have in the tool? It's a pretty popular part that people use, right? You have the embeddings, which are really helpful for the curation finding which samples, finding those labeling mistakes, especially with the cool plugin that Pravin got you guys and fixing it like pre-training. But then post-training, when you then wanna figure out and see where the model's failing, then this is like a super helpful tool as well. Finding out the false positives, the false negatives and seeing if there's any patterns there. Sometimes people will go through the model evaluation, find out, oh actually the model's, right? Our labeler made a mistake. So the error that we're seeing is actually in that, it's not the model actually the model's kind of, right? It's actually we need to go fix our annotation and that's how those numbers improve, Right?

16:08 Laura Chrobak
Yeah, it'd be really cool if it helped you to focus your attention. I feel like for instance, one thing I'm always wanting is I don't think it takes a rocket science genius to like pull apart a fusion matrix, but it does take time. It'd be really cool if this tool could like highlight areas for you to look into somehow.

16:31 Sid Mehta
Yeah, yeah. One thing that's here is that, so for every eval run and it, it's been a while, but you notice that there'll be these new fields that show, which is like the true positive false positives, false negatives. So you can also then filter on these fields to find which are the ones that have, yeah, I think it counts the number. Well I guess for yours, right, it's not multi, you're not doing multiple classification, right? You're just doing, it's just one label per image.

16:56 Laura Chrobak
We can, so basically the, you know, because of the nature of the classifier, you have a confidence for each output and then you just select the highest. So theoretically we could upload all of them Right now, like multiple class for classification I think.

17:13 Sid Mehta
I'm not sure if we support multiple classif classification. So if it is one sample for label, it's perfect. But basically you can kind of use this pretty quickly, this filtering to find out which are the samples that have a false positive or, or a label on there. So that can make it easy then to fi find those ones. And then you can also, you know, based on the model predictions, right? Hopefully you're also finding the loading the confidence values as well. So it's, that's another thing a lot of people do is that they look at the samples that the model was super confident on and, and and, and it was incorrect. So that's a pretty common workflow that we've seen. And so then they'll, and then they'll save it as a view, hey this is like my model predictions like low, low high con or low high con false positive view. And then they'll like look at those samples and see what's going on. Is there something that, that we can do to improve the data there?

18:09 Laura Chrobak
Cool, cool. I can't wait to try it out.

18:12 Danelle Cline
Yeah.

18:12 Sid Mehta
Cool.

18:14 Laura Chrobak
Do you think w would you be prepared at all to talk about the GP resources today also?

18:20 Sid Mehta
Yeah, so yeah, I can talk to it. So I'm trying to think about for your use case though, to be honest. So like for example, when you run embeddings, we, and you go through our input form here, you can you, it'll like, you select a model and then that's where like, you know, it can help in a running embeddings on this data set. And then once it hit execute here I can select if you select yeah like that this model, this embeddings visualization, which is using model inference under the hood will run in their GPU. Similarly, we have like some other functionality like for example the auto labeling features that we have. These use open world models. But again, you can also schedule those like you, I know we looked at the bring your own labels, but like you have something where you, let's say you wanna use it on yeah. Detection model and again, so that these are like workloads that would benefit from A GPU, right? 'cause you're doing this model infants and whatnot. The one thing that why I take a pause with you guys is because I know you have a lot of custom models there, right? So like all these things that we have right now are using open world models, which might not be the best models from your use case from what I understand, right? Because even the embeddings realization.

19:37 Laura Chrobak
Yeah, I mean Well we start, Go ahead, go ahead.

19:40 Danelle Cline
Well we start to be fair, we start with open world models when we do our initial pass at the data.

19:48 Sid Mehta
Okay.

19:48 Danelle Cline
So it, it's not that they don't work, they're just not very domain Yeah. Specific.

19:55 Laura Chrobak
Yeah, they're, they architecture is exactly the same. We just have different weights and classes. So is there a ability to upload our own, even if it's the same architecture?

20:08 Sid Mehta
So I guess in some, in the, so the two built-in workflows, I, there's not that moment yet, but I think that's a really good ask. Now what we could do is that we could create like a plugin. So for example, like we have this plugin, do I have it on mine or do I have it on? So we have this like plugin called the YOLO V eight trainer. And there's like who one of, one of them is, if you wanna fine tune your own model, that's fine. But the other one is that if you wanna do run apply model on a YOLO V eight model on this dataset, right? So here, like you can imagine you're giving it like some cloud file weights and then you're gonna tell it populate this production field and then you would run this on a comp device. So this is like a plugin we built with 'cause for this ask where it's like, hey, I have these like model file paths and you know, I would love to run inference on it. And then with this, again you can run this and then you should be able to schedule schedule GP on there. So we have this solution and I can let, let me show you the code actually. So just So you know, it's not just, it's not just is it specific to YOLO or is it just Yeah, This one is, but then let me, so with the, that's the nice thing about our plugging frameworks is that you can take this and just like customize and come in with your own inference code and then everything else will be very similar, right? So like in this code snippet right here, this is what model inference looks like. Where is it? So you, you would have to take something like this and then just modify it to your use case to your Zoom model. But like, so basically how model inference works is that we have a dataset dot apply model and you give it a model and a label field and that's it. That's all you need to do. But that's only for models that are in our model zoo, right? So YOLO VI is in this model zoo. So that makes it very easy. Now we have a lot of other customers who, you know, work with models that aren't in our model zoo. So they'll just come and then they'll just write a nice little script here, like an infant script here and then that's how they get it to work. They get this plug in to work for them and then they can use this for GPU compute. So I guess like the first question I would have is like if you want to go down this like route of, of like this is like your model that you have, like is it like, is it a model that's in our zoo? 'cause if it is, then it's very simple, then we just need to change some of the underlying code here. And then the infant's code is literally this apply model, then it's very easy.

22:23 Danelle Cline
But even if it, if it wasn't, if let's say we have it in hugging face, which is popular.

22:28 Sid Mehta
Yeah.

22:28 Danelle Cline
And we could rewrite this plugin to just pull from hugging face and then it would just work, right? There's nothing unique. Yeah, yeah.

22:37 Sid Mehta
Yeah. I don't think that it would be too much of a, of a lift, hardest lift because anyways, like for example, to use the model eval, you want something that gets your model predictions in anyways, right? So it'd be taking that script, making sure that script works with the GPU and then I feel like, yeah, once we get there, so our GPUs, it's, it's kind of a relatively new feature, but for managed customers basically. And then we'll have to go, we'll have to bring in probably AZ to talk about the pricing of model. But it's at least the model is you pay as you go. You pay as you use, right? So it's not like a, it's, there's some rate which is like, okay, if you use the GPU for X amount of hour, right? You know how this cloud spending is. It's something similar to that. So it's just so it's not like you're paying for something always on, but you're only charged for as you go.

23:20 Danelle Cline
So that's basically what the Gt Yeah, it it could be, it could be really helpful to have it integrated so we can do this iterations quickly.

23:28 Sid Mehta
Yeah, yeah. Yeah.

23:29 Danelle Cline
I mean we can train a model. It's not that hard for us to train a model, but that's sort of do the evaluation and do the active learning part of it. That takes time.

23:38 Sid Mehta
Yeah. Yeah, yeah, Yeah.

23:39 Danelle Cline
That's where this, this could really give us a, a speed up and performance improvement, right?

23:43 Sid Mehta
Yeah, definitely. Yeah. So I think one thing, so it sounds like we'll probably want to go the custom model route, right? Where you have like a plugin that does it and that uses GPU compute, which is good 'cause we can start working on that right now. I guess in the meantime Pravin and I can go back to AZ and ask him to like share because like just to share the pricing with you and making sure that this is okay. 'cause I feel like that will, because like you, there's a bunch of workloads that you could use this for, right? It's uploading model predictions is probably the highest priority for you. You can also use it for embeddings, right? You can go to one of our, as I was showing you can come here, you can go to embeddings and then you can run your own embeddings run with some of our world models as well. You can also probably build a plugin for example, if this doesn't work for you, you want to do it with your own model, we can also talk about a separate plugin for that.

24:29 Danelle Cline
So, but yeah, that's basically what the gt Yeah, I, I mean I guess I could just stay with this just for a little bit longer. I think that, you know, in our workflow it's helpful to, to do an initial pass at the data with a clustering algorithm that we have that uses an open world model. But it is an algorithm at the end of the day. So it, it, it kind of fits into this. And then now we have a, a cluster we can assign. Now we wanna go back and train a model after we've assigned those clusters. And it would be super helpful to have it all integrated. Yeah.

25:06 Sid Mehta
Right.

25:06 Danelle Cline
Yeah, that would be, that would be it. But we don't, having said that, we don't do this that frequently, right. Probably because we have a lot of friction and iterating. Yeah. Because our tools are kind of fragile. So Yeah.

25:18 Sid Mehta
Yeah. Be helpful.

25:19 Danelle Cline
We're Also helpful.

25:20 Laura Chrobak
Not like, I'm not tied to the architecture. We're using the, I think our problem space is not architecture limited, it's training data set limited. And so if we wanted to use this yo V eight plugin, that would be totally fine with me.

25:39 Sid Mehta
Yeah, yeah.

25:40 Laura Chrobak
I'd, I'd like to test it out.

25:42 Sid Mehta
Got it.

25:42 Laura Chrobak
Yeah, yeah, yeah. So it would be cool for us to just, once we've done that refinement iteration to use the existing Yellow V trainer to assign the split and and train using the resources you guys have.

25:54 Sid Mehta
Yeah, I think, yeah, I mean that's cool. Yeah, that makes also perfect sense as well. 'cause yeah, like, like I said, there's two functionalities to this. One is the train the model, which is like basically fine tuning on your fine tuning a something on your data set and apply model. So yeah. And then both of them can be customizable, right? So you can choose this one if it works for you. And then the only thing I'll have to look at, which we might need to change is that this was mainly made for like object detection labels. You guys are working with classification so there might need to be some tweaking that we need to do to get this to work for you. But yeah, I mean like, you know, if you're not married to anything like this is great and what's nice is because again this is the on 51, right? You can train the model within 51 and then you can then bring the model predictions back so you don't even have to leave the platform. So yeah, we do have some customers who use this. We, this customer used YOLO V eight so that's why this is the initial prototype. But the idea here is like they can come and bring their own models or what if they want to use this one, that's also great.

26:53 Danelle Cline
Yeah.

26:54 Sid Mehta
Yeah.

26:54 Danelle Cline
It's just like yellow 26 now or something.

26:57 Sid Mehta
Yeah, you're right. Yeah, I know we're, we're out, we're outdated with this one.

27:00 Danelle Cline
So I'm not a Fan of yellow. I don't think they're great, but that's Just, yeah. Yeah they're, I like, I like the robo flow models. They're better.

27:08 Sid Mehta
Yeah. So like cool. So let's do that. Let me, let me Pravin and I can ping AZ and let you know about the GPU pricing if that's like something to opt on. Great. And like I said, the cool thing it is, is that it is only, you only get charged what you use. So like even if you don't use it, it's great 'cause you know you won't get charged, right? So that's kind of probably the next step there. And then, yeah, I think maybe we can start, so I can send you this like plugin and you guys can like download it and whatnot, but there might just be some tweaks that we'll might need to do on our end between, and I'll have to see. But yeah, that's basically like, it's a good starting point nonetheless. 'cause it kind of shows you like what's possible. Like this is a really cool workflow where you can fine tune and whatnot. So it's a good thing to ba base off of and we can just customize it to your use case. Yeah.

27:54 Laura Chrobak
One thing that would be really nice or particularly attractive about this is if we trained within this interface, if there was a model card that referenced the state of the data that we trained on.

28:09 Sid Mehta
Mm oh so like lineage. Interesting.

28:11 Laura Chrobak
Yeah. I'm not sure that that, that probably doesn't exist. But just like in case that, yeah, put it on the radar, like that would be really attractive because one thing that we struggle with internally is just keeping references of what was used for each iteration and Got it. If we're going to, like, we already have resources here so we can train it here, but the added benefit of doing it within the same ecosystem is if it was traceable.

28:38 Sid Mehta
Got it. Got it. That's one thing that's helpful with the delegated operators is that if you go to any runs page here, I don't know if you've noticed, but oh what happened there? But you notice that like, 'cause it will run it as a deal runs. So you can always come back and see that, like what was the input here? So that might be helpful. 'cause I think we all, you can also see maybe what view it was trade on. So we do have some traceability, but yeah, that might be also something we can maybe add to this plugin. Maybe it also stores it somewhere in S3, right? It takes like right Samples. Yeah. Or or something like that.

29:10 Praveen Palem
Yeah.

29:11 Laura Chrobak
It stores selected metric plots with it just so you have a reference or something.

29:15 Sid Mehta
Yeah.

29:16 Laura Chrobak
Cool. Yeah, we, so this week we're, we'll spin up our workflow for the review. I think we have everything from you all as we need it. But we'll keep you posted in case anything comes up. Okay.

29:29 Sid Mehta
Yeah.

29:30 Laura Chrobak
And if you can make the change for this plugin to be classification centric, we'd love to test it out. Yeah. Do you have a question? Pardon?

29:41 Praveen Palem
Hey. Yeah. Hey guys. So I think, I think this, this ties back to the question I asked in Slack and it's great that now we're talking about not just running evaluation but also training the model in 51. That's great news. So I just want to make sure we kind of think through the whole pipeline, right? So potentially we're talking about bringing in training data, which is, which is, which is supposed to be a lot larger in size. And then you build your model or fine tune. And then would you be also interested in doing the clustering also in using one of our models Or, yeah.

30:20 Laura Chrobak
So a slight change to that because we have so much data, I think we'd wanna do the training on the labeled set. So what I'm imagining us doing is we have our deployment, we internally run our classifier and upload the, the machine predictions that we want to box all 51, which is probably a subset. It's like probably gonna be anything over a specific competence threshold. Okay. And then we maybe refine those, add it to like combine it with a previous dataset and then train on that subset label. So it's, it's not actually Okay. We wouldn't be using this infrastructure to run on the full collection because that's probably, I mean we could if it's cheap enough, but Yeah, I mean we could, we could potentially look into that.

31:24 Praveen Palem
I mean I, I-I-I-I-I guess I would, I need to, we would need to know how much it costs for you to write it on your own hardware versus, like likes said, we would get, get you some metrics from AZ and we could, we could compare the costs, right?

31:37 Danelle Cline
I think that's probably worth doing. Yeah. And just a, just a data point on this. Yeah. We had one of our internal scientists use the community version to look at about a million ROIs and to do this process of validating the model output, it was pretty hard. I don't think she looked at all of them, all the points.

32:04 Praveen Palem
Hmm.

32:05 Danelle Cline
It's just a, it's, it's sort of, that kind of gets beyond the human capability.

32:10 Praveen Palem
Yeah.

32:12 Danelle Cline
And that was, that was just a one deployment and we have many of those that are much larger. So we really need to think through that. I think Laura's idea is only loading confident t confident predictions probably one way to filter it to, i, I don't know. What is the one thing I grapple a little bit with is what do we do with really rare predictions, which might not be very confident, but they might be really rare and important.

32:42 Praveen Palem
Hmm.

32:43 Danelle Cline
And so finding ways to figure out how we define those, like either heuristically or through some kind of algorithm. 'cause those can be important for the science. It doesn't necessarily mean the model's gonna predict them.

33:01 Praveen Palem
Right. So, Okay, got it. Yeah.

33:06 Danelle Cline
So we need to, we need to think through that a little bit to, Okay.

33:11 Praveen Palem
Okay. Got it. So, so let, let, let, let that, I'll take that as an action item. And the second thing is, right now you're uploading your embeddings, right? You're generating an embeddings in your system?

33:23 Danelle Cline
Yes. Yes.

33:24 Praveen Palem
Okay. Is, is that also potentially something that you would want to do in our platform?

33:31 Danelle Cline
Sure.

33:33 Praveen Palem
Okay. Yeah.

33:34 Sid Mehta
Yeah. That one might not be that hard I guess as well. 'cause if you already have the code for it, it might not be hard to take it as a plugin. So, and yeah, as long as your code can make it so that it, we, it runs when the GPU is available, we can bring in the GPUs. So yeah, there's like, there's a couple different ones. It might be good to say like which one you want to try first. 'cause you know, this is like a good thing to like rid your first plugin and like, you know, if you already have like a script that kind of does a lot of it, we can kind of test it, test the GPU also is working if that's an easier use case. And then just fine tuning one 'cause and, and, and model tuning. So whatev whatever you guys want, we can kind of work both in tandem. But yeah, we can also show you maybe next time what are good ways for you to like test these plugins locally and then how you then upload them to 51 Enterprise. So then you can then everyone can use, right? So if Laura's developing something or takes something or wants to change something, she can edit it. She can test it locally and then she can upload it for everyone. So all all the other free users can use.

34:38 Danelle Cline
Okay. Look, Laura have you, you We'll yeah, we'll go back to you on that Laura and I can chat about that offline.

34:44 Sid Mehta
Oh yeah, Yeah. Laura, I know you have used 51 open source, but did you ever develop your own plugin or not?

34:52 Laura Chrobak
Not that I provided to the public.

34:55 Sid Mehta
Okay. Okay. No, but even just internally you had, were you able to do one? Okay. Yeah. Yeah, that was good. So I think like a, a good way is always you start with some Python script, right? That's generally good starting point. Once you have that, then you do it into a plugin generally for, and then we have a way for you to like debug within the, even with enterprise, there's a way to like debug so that you can like it's much easier, which is what I'll show you next time. And then, and then that way you can test it and then you upload it to 50 to an enterprise. So it works. And then with our compute.

35:25 Laura Chrobak
So that Reminds me, did you have instructions that I might've missed for the MCP server for writing plugins?

35:40 Sid Mehta
Yeah, that is, I think, yeah, we can pass that over Pravin. 'cause I think Ed and I, our docs guy has done some work on it. So yeah, I think we'll, we'll send those after a follow up for this meeting.

35:50 Laura Chrobak
Cool. Yeah, it's not like immediately necessary, but it would be good to have reference.

35:55 Sid Mehta
Okay, cool. Yeah. Yeah. So on our end we'll send you the GPU some stuff from AZ and just so you guys have that information, just so make sure you it's okay to opt in and then yeah, it would be good for you to tell us, I guess soon, like which direction you wanna go first. Do you wanna try bringing in these embeddings your embedding model and seeing, and we get that as like a POC to test this GPU work stuff? Or do you wanna do the fine tuning and apply model one that I showed you and use that and maybe we, we work on getting that working with classification, I guess let us know which one to maybe prioritize first and then that, that would be like a good way for us to like start this G Ps story.

36:36 Danelle Cline
So Laura, do you have everything you feel like you need to, to move things forward on our end with?

36:42 Laura Chrobak
Yeah. Yeah, we just need to schedule it.

36:44 Danelle Cline
Okay.

36:45 Praveen Palem
Okay.

36:45 Danelle Cline
Perfect.

36:47 Laura Chrobak
Yeah, that sounds great. Janelle and I can kind of sync on what direction we wanna do. Okay.

36:53 Praveen Palem
Okay.

36:53 Sid Mehta
There.

36:55 Praveen Palem
Yeah. Got it.

36:56 Sid Mehta
Got it.

36:58 Danelle Cline
And just so I understand, like our scope of our, like our timeline, how much longer do we, do we have your support?

37:08 Sid Mehta
Oh, till, yeah, till. So yeah, I mean like generally what happens is that like we meet you guys meet, keep meeting with you guys till you don't wanna meet with us. Because generally what happens is that like as you're onboarding and spinning up these new workflows, we meet more often, but then like, we're still always here. But generally what happens is that like you guys are good. There's not that much to talk about. Okay. So like, yeah, we're, that's our support never dwindles, but like, it never dwindles because we say so it's just naturally right. Cut. People get busy, things are good, things are well, right. We're obviously building a lot of stuff, but once the stuff is built kind of works, you know, so it's just maintenance in case anything breaks. We're always here, but like, yeah. So it's, it's pretty natural. Like there's people who I met like a lot the first two months and then now they don't wanna talk to me for some reason.

37:51 Danelle Cline
I don't know why, but, Well, Laura has some travel plan next month, so Yeah, yeah, yeah. We just have a few more weeks and then Yeah.

37:59 Sid Mehta
Yeah. So we'll definitely try doing it. Try to get then yeah. Okay.

38:05 Danelle Cline
Cool.

38:05 Sid Mehta
But yeah, let us know also when you, if you get a chance to try this model eval stuff and if you have any questions as well, that's also a good thing, getting your first model eval run is like a, is a good milestone As well.

38:14 Danelle Cline
Yeah, for sure. Yeah, we should talk about that, how we can exercise that.

38:19 Sid Mehta
Yeah.

38:20 Praveen Palem
And, and yeah, whenever you guys can sync, please let us know what in, in the order of priority. I'm guessing it's gonna be the eval, custom using a custom model and then maybe training a model. And then maybe third would be the embedding or you know, just, just like Come up with a priority list so that we can go.

38:38 Danelle Cline
Okay, sounds, sounds like a plan.

38:43 Sid Mehta
All right. Take care guys. See you next week.

38:45 Praveen Palem
Thank you.

38:47 Sid Mehta
Feel better.

38:48 Praveen Palem
Thank you. Yeah, bye.
