## 2025-12-18 - MBARI Sync

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/60e8141a-c367-4848-9365-25ffdf7bf3f4

**Voxel 51 Participants:**

- Praveen Palem
- Eric Hofesmann

**MBARI Participants:**

- Laura Chrobak
- Danelle Cline

**Meeting Notes:**

- Demonstrated bulk label editing workflow using "edit field values" plugin (lasso selection → filter → change labels)
- Discussed challenges: requires 5+ clicks per change, workflow optimization needed for large-scale review
- Introduced custom plugin development to streamline bulk operations
- Covered confusion matrix interactive features for identifying mislabeled samples
- Demonstrated annotation schema configuration (constrained label dropdowns, custom attributes)
- Discussed label reconciliation for hierarchical taxonomies and preventing spelling errors
- Introduced snapshot feature for dataset version control and rollback capability
- Covered histogram visualization and "last modified" tracking for change management
- Addressed community version session timeout issues (likely networking/firewall related)
- Planned custom plugin for bulk label changes and database synchronization

### Transcript

00:02 Eric Hofesmann
Hey buddy.

00:04 Praveen Palem
Can you guys hear me?

00:05 Eric Hofesmann
Yes. How's it going Laura? Great to meet you.

00:11 Laura Chrobak
It's going well. How are you?

00:13 Eric Hofesmann
Also pretty great.

00:16 Praveen Palem
Did you, did you recover, recover fully, Laura?

00:18 Laura Chrobak
I Think I have not. Fun wood. I thought I did yesterday and I was definitely overly optimistic. I don't know, I just got hit by a train virus wise. So Yeah, Stay safe out there. Don't, yeah, hide. Don't talk to anyone.

00:39 Eric Hofesmann
Stay away from strangers. Oh man. Yeah, it definitely seems like something's going around, like a lot of people are just Yeah.

00:48 Laura Chrobak
Coming down with colds, so, Yeah, apparently California has like a higher rate of new viruses than all the other states do. I was sick times, but apparently we get a lot of exposure to new viruses.

01:11 Eric Hofesmann
Interesting. Hey Andrew.

01:16 Praveen Palem
Hey Andrew.

01:18 Eric Hofesmann
Hey left.

01:22 Praveen Palem
Alright, let's, let's give Danelle a few more minutes maybe.

01:27 Laura Chrobak
Yeah, I'll ping her. Okay. Yeah, that being said, I have not had time to, in a focused way, re-watch last week's meeting. I attempted it and then determined that I was too sick to continue.

01:44 Praveen Palem
I don't believe you.

02:04 Laura Chrobak
Okay. I messaged her. Maybe we can give her two more minutes and that in the meantime, do you wanna just give me a brief overview of what you covered last week?

02:16 Praveen Palem
Yeah, I can do that. Basically we, it was basically our kickoff, official kickoff and we went through the SSO user management, you know, loading data into, into the tool and we pointed, you know, Daniel towards, you know, the links and, and, and, and you know, on Slack everything is like, if you go back in history you should be able to see all of the things that we discussed. But essentially with Andrew we discussed the credential management and there were, there was a need for programmatically also rotate, rotate the keys that we pointed him to, to where he could add and remove credentials using the SDK. And there was also a discussion around database synchronization potentially where changes made in the app. We want to be able to save into the, into your database and that might need a custom plugin. So that was something also we did, we discussed and then we, we also did talk about, oh, there just Elle. Alright. Yeah. And Hey Danelle. Hey Danielle, You're muted.

03:40 Laura Chrobak
Better? Yes, Much better.

03:44 Praveen Palem
All right. I don't know if everybody met Andrew, Eric, but since it's Christmas time we brought in the special guest and he is one of our most senior, senior most MLE success engineers in the company. So, you know, we were, we have him here to answer anything and everything against, to the product.

04:03 Eric Hofesmann
Yeah. Thanks Pravin. Yeah, great to meet y'all. Yep. You can tell beard still needs some growing not Santa Claus yet, but just brought in for the holidays. Yeah. I'm also the machine learning engineer, one of the founding engineers of OX 51, also on the customer success team with Pravin and Sid. And yeah, just joining to chat about what you guys are doing and help. Cool. Any questions you've got. So super excited about all the work that you guys are doing. It's, it's really awesome getting to work with y'all, so this is fun. Yeah, great to meet you all.

04:34 Praveen Palem
Yeah, So I was just catching up Laura on what we discussed on Monday. Danelle. So yeah, so we, we were, we were at a database synchronization where we, there's a need to potentially write back changes from the tool of your database. And then we talked about embeddings and delegated operators and potentially using a dino model that suits best for your work. And, and then we did cover the model evaluation features in the tool and also annotation needs. And so we did enable the annotation feature and we could, we could potentially like, you know, walk you through how you would do that today that Could be productive to do that, I think.

05:19 Danelle Cline
Awesome, awesome. Because we could probably th rush around and figure it out, but Yeah, I'd rather not.

05:27 Praveen Palem
Yep, yep.

05:28 Laura Chrobak
That's In my like vague haze of watching this. I remember a bulk discussion about more bulk review features and maybe some challenges with that. Could you kind of give me some detail there? I know that I'm cog more cognizant.

05:48 Praveen Palem
When you say bulk review, you mean like bulk updates?

05:53 Laura Chrobak
Yeah, like bulk grid-like view of all of the annotations and maybe like making changes to those labels or rejecting them or, Yeah, yeah.

06:05 Praveen Palem
So, so bulk annotation changes may to to to to to bulk select selected images and changes to annotations is something that's in the pipeline. And, and I did clarify with Danelle that you, you want to update labels in bulk. So that's, you know, that's we, we are talking with the product and it should be, you know, we'll, we'll we'll put pressure on them and get it done for you guys soon. But that's definitely coming down.

06:33 Laura Chrobak
It's possible though right now to use the like cluster point and click feature to rename a subgroup though. Right. When you say rename a subgroup, Like let's say I'm, I am viewing that cluster, I pick a subset I see, I know that, I see that grid on the left hand side can, if all of those, like let's say what I've clicked on is I want to rename all of those, can I take that action?

07:03 Praveen Palem
Reclassify them?

07:03 Laura Chrobak
You mean reclassify? Yeah. Re change the label name Change.

07:07 Praveen Palem
Yeah, I think that's possible, yes. Okay.

07:10 Danelle Cline
Yeah, it's, it is possible and although I have tried, I have done that to tag, I haven't tried to do that to actually change the label, but I presume it's the same kind of operation.

07:29 Eric Hofesmann
Yeah, so we do actually have this, it's called edit field values. It's one of these like kind of plugin operators that is available in 51. So this isn't like officially pardon built into our annotation feature site yet. Like Pravin mentioned, it's still kind of in development. Okay. But there's a ton that you can do with these plugins and this is something that's come up a lot. So just for example, taking a, like a classification field, which I believe I saw that you're all working on, you can select the field that you want to kind of edit and then you can choose whatever class that you want to change. So like if I want to rename all my cars to, I dunno vehicle, I can do that. I can then say I want to take all the cars that are currently in my view and then change them to vehicle.

08:16 Danelle Cline
Oh, I see. So that's like a global edit, right. I think what we're, what we're really more near term we'll be doing corrections, right? Yeah. We'll be some, some errors and yeah. Yeah, just doing that quickly. That's, Yeah.

08:35 Eric Hofesmann
And this doesn't have to be global. So like this can be whatever subset of Data.

08:40 Danelle Cline
Okay. Well slow down a little bit. Let's walk back.

08:42 Eric Hofesmann
Yep. Walk me through That. Yeah, so basically let's say that we've got some data here.

08:48 Danelle Cline
You, You just do your lasso, you get the query.

08:51 Eric Hofesmann
Yeah. You can lasso that. You can let this shows there's 23 selected so we can, there's 23 samples right? That we're looking at out of I think 10,000 dataset. Okay. So then if you click this browse operations, there's this edit field values actually remember if that's built in by default or if that's something that can be installed. But actually let me just double check that quick. You might be able to just follow along with this if it is built in, which would be awesome. I've just got another deployment pulled up here. Okay. Yeah, it looks like it actually is built in, so you should be able to do this actually here. Okay. We can run through it on your side live, but just real quick, what you'll look at here is after you click it you can then select just the current view. So this right here means that we're only gonna edit these 23 samples Actually. Okay. And then you can select the field. So like my ground truth field, in this case with my labels, I want to relabel some class that I have to a different class. So I select a field that has those labels and then I can select the actual like class value that I want to change. So in this case, if I want to change all of my, you know, buses to, I don't know, vehicle or something, I can do that. Awesome, thanks.

10:14 Laura Chrobak
Yeah.

10:15 Eric Hofesmann
And we can, we can also try running through that on your side if you want to share.

10:18 Danelle Cline
Yeah, no, I, I thank you for that. I, I guess just some sort of observations in walking through that to change a label, I'm gotta do like five clicks and five changes for every change. So that feels like a lot to me. And if I, tagging is a little bit more straightforward 'cause it just works, right? You don't have to, when you lasso the collection is there from the query and then you could just say tag it. The problem with that is it's fast but it doesn't really reflect in the, in the, in the, in the plot. Or at least I have, I haven't figured how to do that. So I mean you need to have some feedback to say I did this already. Help me understand that.

11:10 Laura Chrobak
I also really am, am very hesitant to use tags for like when we're dealing with all of these classes, our biggest issue is that some expert types, something slightly different and then we can't reconcile or Yeah, well I don't know if I would, I think I would just say it's, I would not agree.

11:31 Danelle Cline
It's a big issue. We, we have to clean the data when it's done. It's an an a nuisance. But I, I think that perhaps the really big elephant in the room is it's really hard to go through these data sets quickly. It's, it's the tools we have aren't very good and they don't work on millions of examples or even hundreds of thousands very, very easily. So like what's the best human computer interaction that we can do to make that easy?

12:05 Eric Hofesmann
Yeah, maybe it's not, maybe it's too much to ask but you know, So like the example here was just kind of what's available outta the box.

12:14 Danelle Cline
So that's where you can actually fancy Can you, can you create like a macro from that or a Exactly How does that work?

12:24 Eric Hofesmann
So some examples there, you can actually have custom buttons here. So you can, this does require like some engineering, like some Python code on your side to build one of these plugins. But you can see a bunch of buttons here that you don't have in your deployment. These are what we call like plugins that allow you to actually extend 50 ones like UI capabilities to do whatever operation that you want. So this is how you can kind of get very like fine-grained functionality for specifically what you want to have happen at the click of a button. So instead of having to go like through this dropdown clicking this, choosing a field choosing value, you could have it so that you just click a button and then it does kind of exactly what you want. Maybe it gives like some selection of like I want this class to be this class and that's all that a user has to actually click. So you can make it as simple as that.

13:22 Danelle Cline
So this, I see, so you could have a plugin for class remapping and then would you have a plugin, let's say we have 20 classes, would it be 20 plugins or would it be one plugin that does them all?

13:37 Eric Hofesmann
Could be either. So that's where it's kind of like up to you like whatever how, whatever you can imagine of like how you want that UI to look and feel is possible to build with just a little bit of, Okay, So probably you wouldn't want 20 buttons, but if you do you could do that. But if you want like one button click and then like, you know from there.

14:00 Danelle Cline
Well yeah, so I just wanna stay with tags a little bit longer. I completely hear your concern Laura, but I'm wondering when you load data, it actually looks at your data set and it gives you a a it parses and says, here's here's your unique classes and it populates these lists based on that. So when you do a label you can, you can have some enforcement of not like it's a freeform field but it doesn't, you don't have to use it that way. Like for the text This short term, could we just do that instead of like, it's gonna take some time to write plugins to make this more seamless.

14:46 Eric Hofesmann
So for this tag, well are you saying like if you stick with tags specifically how far you can go with that? Yeah, so at the moment the tags are always going to allow like the freeform input.

14:58 Danelle Cline
Okay.

14:59 Eric Hofesmann
Yeah. So there's no way to disable that and have it just have a fixed set of labels that is often the very first plugin that people end up building 'cause it is a very like simple one from what's needed from the programmatic side and also just a pretty common like use case. So yeah, that might actually be a good next step. And that's something that like the customer success team, what we are kind of here to help you with is like putting together examples of what these types of plugins look like. So we can put together for example, some boilerplate of like here's what you know is one way that you could have this custom like class changing plugin look like and then hand it over to you and then you can just kind of modify it to look and feel exactly how you Okay. So you don't have to do The whole thing.

15:46 Danelle Cline
I think that's pretty important for what we're doing. 'cause we have, you know, as we said in our last call, taxonomic things can be pretty tricky and easy to get wrong and say no some even, you know, they put a white space in the wrong spot and you go on.

16:04 Eric Hofesmann
Yeah, totally. And it just messes up your whole schema.

16:07 Danelle Cline
It's just an, it's just annoying. Yep. So having the schema would be better, but I don't see that as priority. But mostly just making this fast so we can go through this for we, we, we really have a lot of data sets we need to process and look at. Cool. And then also, I mean Laura's I'm sure will have some good performance improvements, right? By looking at the, the integrated model tools are, they're pretty cool. I mean the, the visualization's pretty cool. I think that's pretty helpful to interactively see your class performance and be able to see what's, you know, where we're getting the errors from and things like that.

17:01 Eric Hofesmann
Yeah, for sure. Yeah, so I would say like we can probably take that as an action item. Pravin from our side is we can try and take a stab at just an example of what this type of like class class editing plugin would look like and then send that over and maybe just have like a session where we just go over what it looks like to kind of create these plugins and how you can update the plugin code that we share. Okay. To do different things. But I guess just high level, can you talk me through it once more, just a little bit more in detail of how you want it to work? So for example, we have this edit classifications button. So let's say that I find something interesting in my embedding plot or somewhere else. I find some labels that are mistakes like in this case these are all nighttime or daytime samples that are classified as night. So we'd wanna fix that. What would you want to have done here? Assuming that there's like a button that I can click like this?

17:59 Laura Chrobak
Yeah, I can walk you through those steps. I think it would be really awesome to do the walkthrough with our data. Is it possible to do that?

18:11 Eric Hofesmann
So yeah, I think, I mean right now I'm just trying to understand like what this plugin might look like.

18:17 Laura Chrobak
Okay. So Yeah, I can walk through it in in this scenario. So essentially, oh Are you okay let, sorry, lemme pull that up one more time.

18:26 Eric Hofesmann
There we go. Yes.

18:29 Laura Chrobak
So we might have all of our different clusters. For instance, I think we have 40 different classes for our current classifier and we might look, we might want Patrick to, or one of our expert labelers to look at an area where we're seeing undifferentiated labels, right? Like there's lots of different colors in the same region and in this case he might go through smaller subsets of that and change those. So there might be cases where the image is, has has a specific label from the classifier, but it's unclear to a human what that would be. So I might move, I would ultimately just wanna remove that from the dataset at large. I don't know what that action looks like, but I want it not having the current label. There might be ones where the label is definitely correct, maybe nothing has changed there. And previous workflows, sometimes we have a verify versus a unify state. But if those are reviewed and you can double like verify something that's helpful or if you see that it's like the label is incorrect, you rename it. So those are kind of the three action steps. Either it's a rejected label, it's renamed, or sorry, a little brain fog. It's rejected, it's renamed or Verified You. Yeah, if that's an option at all. I think that all of the ones that we'll upload for the main dataset will have been verified by Patrick. But this thing kind of goes in cycles, right? He might have verified last time and then we reset it to null and this is a second round.

20:39 Eric Hofesmann
Got it, got it. Okay. So there's real, there might actually be like three different buttons here then depending on like, you know, as he's reviewing these, depending on what should happen with certain images and certain labels, there could be a button that says like reject that will then just maybe like remove the label entirely or like delete the sample from the dataset. That could be one action. Another action could be wanting to change the label to another label. And is that usually a label that is already like predefined, so you don't want it to be able to be a free text input?

21:15 Laura Chrobak
Ideally, yes.

21:17 Eric Hofesmann
Got it. Okay. So you can like click a button and then say like, I want this to be labeled as something else. And then you would want to do that in bulk though, is that right?

21:29 Laura Chrobak
Not necessarily For, yes, I would definitely, yeah, that would be in bulk. I'm imagining for instance, in some cases there maybe you have a really cohesion, sorry, a, a really homogenous cluster, but there's one or two that are clearly differentiated and you need to take this action for, maybe those are one-off cases, but there are other cases where it might be 50 50 split, in which case you're doing it in a larger way. And also that review action is less important to us than the previous two of bulk rename and reject.

22:09 Eric Hofesmann
Got it. Got it. Okay. And out of those two, which one would you want to start with? Editing or rejecting?

22:16 Laura Chrobak
Definitely editing because we could create a fake name that says rejected and just not use those in our training.

22:26 Eric Hofesmann
Good call. Yep, that makes sense.

22:27 Danelle Cline
Good idea. Awesome.

22:30 Eric Hofesmann
Okay, so the idea would be then for like whatever labels are in view or potentially if there are certain, like, you know, some subset of them that are selected, be able to have a button that can be clicked and then maybe like a single dropdown with the available classes that you can then click and then say, okay, rename all these classes or like reclassify all of these labels too, this new class. Awesome. Yeah, I mean if that sounds good then I, I, there's definitely a number of different plugins that we've got that are kind of close to that. So Pravin, I think we can probably take one of these, like this edit classifications for example is probably a good starting point where we can take that, put together a proposal for what that would look like for your case, and then we can start from there.

23:20 Praveen Palem
Yeah, sure.

23:21 Danelle Cline
Great. Sounds good.

23:28 Eric Hofesmann
So Yeah.

23:31 Praveen Palem
And, and then reject means you remove the legal from right? You want blank, is that correct?

23:38 Laura Chrobak
Yeah, yeah. We have a lot of ROIs that are essentially und discernible from a human perspective as to what the class is. And that is our qualifier for if they're used. If, if a human can't tell, then we won't include it.

23:55 Praveen Palem
Okay.

23:56 Laura Chrobak
Does that make sense? So we so it, the, the classifier might have thought that it knew, but upon the human review, so, so we run this classifier over it, we get a label for every image and we're not really using a confidence or anything that's above the confidence threshold that we select gets put into voxel 51. But not all of those are necessarily good observations. And so for the subset that we want to remove, because we can't even tell what it is, we need to be able to get rid of that data.

24:31 Praveen Palem
Got it, got it. And is this third verified phase, is that, is that something like a tag you want to show up or is it just like, if, is it by default understood that it's very verify?

24:43 Danelle Cline
So yeah, I think that That, that kind of falls maybe into more like an attribute because it, it hangs along with it to, you know, so we know whether we can use it or not for training and yeah. Yeah, makes Sense.

25:01 Laura Chrobak
I would prefer us to focus on the first plugin that review toggle. It can introduce more labor because for instance, let's say I've uploaded a bunch of imagery and I've only reviewed a portion, then as the the receiver of that data, what do we trust? And so then I would need my reviewer to actually go and review everything and we don't know if that's part of the pipeline yet, so let's focus on the first plugin adoption that we've discussed, which is rename and then we can get to that next step. 'cause I think in terms of like the goals that we set out, refining the existing labels was kind of our, our first big action item. And so that plugin will help us get there and I think that that is the only capability that we would need in order to tackle that, that task Sounds good.

26:06 Praveen Palem
Yeah, we, we will start, i, I will get started with with that first action item for the plugin and then I'll keep you posted.

26:14 Laura Chrobak
Awesome.

26:16 Praveen Palem
All right. Do we wanna switch gears and look at the human annotation? Danielle? Oh go ahead.

26:23 Laura Chrobak
Look, One view that we would love to leverage in addition to the, this workflow that we just went through in terms of the clustering view is like potentially a confusion matrix view. And I think that maybe I had seen something like that. So similarly, rather than having Patrick like go through the cluster world, it would be awesome if he could look at specific confusion matrix boxes. Is that something like a workflow we could discuss?

27:02 Eric Hofesmann
For sure. Absolutely. Let me pull up an example for that.

27:07 Danelle Cline
So Help me understand, you're like talking more like interacting with the confusion matrix down Like on one of these, everything that's within that box.

27:22 Laura Chrobak
And this is a really nice way for, for us to expedite and clearly it we're incorrectly labeled.

27:35 Danelle Cline
And so that's, that's built into the, is this a plugin? The model evaluation?

27:39 Eric Hofesmann
This Is actually built in. Okay. Yep. So the way that this works is it assumes that you have two different fields on your dataset. So a ground truth field and then a predicted field. And then it allows you to basically evaluate your predictions in whatever field those are in against the ground tree field. And then you can kick this off and depending on like the type in your case, I assume it's like image level classifications, right?

28:10 Laura Chrobak
Like Every image all Got it.

28:13 Eric Hofesmann
Yeah. So it'll basically do that evaluation and then store the results on the samples. So it'll tell you all of the false positives, true positives on each of these samples. And then it'll populate this model evaluation like these results where you can then click into the evaluation results for that run of model prediction versus ground truth. You can see like the high level stats of like the accuracy of the predictions versus ground truth. And then one of these is this confusion matrix, which is interactive. So it'll then have all of like the predicted classes on one side, all of the ground truth classes on the other. And then, yeah, this is basically like how many samples of a certain class had this ground truth label in this model predicted label. So for a good model they'll all be on the diagonal. And then these off axis elements is where things get interesting, where you'll have like, you know, the prediction of cars, like the ground truth label of bus. And then since this is interactive, I can just click that cell and, and exactly that class confusion.

29:23 Danelle Cline
So in your case, you know, Be nice to be able to do that interactively. That's very helpful.

29:28 Eric Hofesmann
And so, and this Is, that could be useful.

29:32 Laura Chrobak
I was sending my question. That sounds great. Yeah, Danelle, this would be not our initial first step. This would, because essentially we need need ground truth labels for these. But Yes, If we had a new classifier and wanted to see where there were errors or whatnot. Cool. Thank you.

29:51 Danelle Cline
That's great. Awesome.

29:55 Eric Hofesmann
Yeah, Yeah, Go ahead.

29:58 Praveen Palem
Laura did you have something else?

29:59 Laura Chrobak
Yeah, I have another question, but I wanted to understand what other things we have on the like conversation agenda so that I can, it's worth slotting in.

30:09 Praveen Palem
Yeah, I think Danelle mentioned the human annotation would be good to look at. So maybe if you guys can start sharing your screen, we can actually walk you through it that way you get your hands dirty and yeah. Okay.

30:19 Danelle Cline
You wanna do that Laura? I think that I'm going, I'm just wonder if it'd useful for you to try to grab my data set 'cause we haven't really tried to share Yes. Works. I Would like to, I will reload it, but what's in there is fine.

30:36 Laura Chrobak
It, you know, explore That sounds, yeah, I'm excited to see how this works. Do you think that you can share for now and I?

30:49 Danelle Cline
Yeah, yeah, yeah, yeah. Okay. Let's see. Is our $4 called 51? I won't for you with the, the details here. Okay. Let me make my screen bigger and I'm gonna unplug. Okay, now I get back to meet, share how I think this is the right one. Go. Yep. You see my screen okay? Yeah.

31:52 Laura Chrobak
Okay. I'm following along on the side here so we can both do It.

31:57 Danelle Cline
Oh, cool. Okay. Alright. So what, what is going on here? Everyone can see your annotations. I don't know if I want that. Like what are we doing here? I guess this is fine. Does this just, does it just work then?

32:18 Eric Hofesmann
Okay, I've got a green dot, but it's not, yeah, I think This is like some weird Google meet. Like you can draw on the video screen feature. Okay.

32:29 Danelle Cline
All right. I don't wanna do that. It was just turned on too. Oh, stop annotating. There we go. Okay.

32:40 Eric Hofesmann
Do you have your computer back?

32:42 Danelle Cline
I have sharing tab. Okay, here we go. There we go. Sorry for the technical. Okay, so let's go to our data set. Sat, and I guess I should split my view of my embeddings with my model.

33:13 Laura Chrobak
How did you Oh, split View. Got it.

33:15 Danelle Cline
Yeah, I just split the view. I'm sorry, I'm going faster.

33:18 Laura Chrobak
Oh no, I'm, I'm, I'm on it.

33:20 Danelle Cline
And then color by, by label. Cool. Okay, so let's just say I got some pink stuff here. Probably not correct. Right. But I first wanna look at it, what's the pink stuff? And it is detritus. I don't know if I trust that, but let's just say, Can you select from the legend? Well where, what do you mean?

34:08 Laura Chrobak
Can you select the cluster from the legend?

34:13 Danelle Cline
Oh yes. You can do it either way, right?

34:17 Eric Hofesmann
Yeah. So like say that you wanna click detritus you, you mean like can you just click detritus and then pull all of the pink ones?

34:23 Laura Chrobak
Yes, you can go so many.

34:25 Danelle Cline
You can, you can also, oops. Escape. And then escape. If I, I did escape twice there and I just double clicked detritus. It shows me all the detritus.

34:38 Eric Hofesmann
Yeah. So another thing that you may want to do, can you double click that one more time? If you click on the left hand side under ground truth and then, so yeah, on the sidebar there under ground truth, click that arrow and then click on label and filter by detritus here this will will actually filter all of the samples and then still should still show like the location of them. Okay. It doesn't quite update that way. So this would be another way to find, see like all the detritus while still seeing all of The, but that's just sort of doing this, it doesn't update the Right, Right. Yeah, no, I thought it would, that's my bad. Nevermind. Use that other side. Yeah.

35:23 Danelle Cline
How did you Jan know, right?

35:25 Laura Chrobak
How did You get it? Janelle? Oh, okay. I'm on board. It's a triple click. All right.

35:29 Danelle Cline
Yes. And if, and I think at any time if you, if you're, if you just escape. Yeah, so for this one you need to clear it out on the left Hand you need to clear out this and then that gets you reset.

35:48 Laura Chrobak
Okay, cool.

35:49 Danelle Cline
So if we wanna do a bulk label, like I think that that's actually wrong. When I look at these, this is ct, I think these are actually cts. So in this case I wanna go in and I wanna select all of these and I want I, I picked up a few of the blue ones, but now I wanna bulk change all of these. So are they actively selected? And then I have to go to operations And then type in Values.

36:29 Eric Hofesmann
Values And then click that edit field values, Edit field values.

36:35 Danelle Cline
Yep. Current view, select the field, which would be It be ground truth label, I believe Label and then I want to change it.

36:46 Laura Chrobak
Yeah.

36:46 Eric Hofesmann
And then you can do multiple values at a time. So you do have to add them.

36:50 Danelle Cline
Current Value is detritus, but I want them all to be silly.

37:00 Eric Hofesmann
And then now if you hit execute, then it'll actually do that change. And then now you can see that we've got a bunch of blue points there now. Okay. If you zoom back into that cluster, there's still a couple pink ones.

37:13 Danelle Cline
Oh let, let's just see. Okay, so now I did correct those, but now I have just a few pink ones and that's what I would expect. Was that the right? Yeah, that was the right one. So it made the bulk change, it updated the map and that's, so that's the bulk change, right? That's it. I didn't have to select everything. It was actively selected. Exactly.

37:44 Eric Hofesmann
Yep. So that's what it looks like today. It just required some extra clicks, but the plugin And then, yeah.

37:53 Danelle Cline
Can you keep that act up here? Like do I have to always click on this?

37:57 Eric Hofesmann
Yeah, you will always need to open the operations. So that's That.

38:02 Danelle Cline
Create a view with that in it or a Yeah, exactly. Workspace It doesn't, doesn't work. Okay.

38:07 Eric Hofesmann
Right. Yeah. That's one of the benefits of then having it be a custom plugin. I mean you can get it kind of efficient. So you can hit like the Tilda key on your keyboard. Oh and then the most recently used one will be the first one.

38:22 Danelle Cline
Oh, okay. So if I go this, I'm sorry.

38:26 Eric Hofesmann
No, yeah, if you just clear out any of the selections. So just on your keyboard, like it's the one under escape usually like the tilda that should open up the Cool, well I got a Mac keyboard, so Ah, I see. Lemme see what that look like on Mac.

38:47 Danelle Cline
But do I need to be within the B browsers?

38:50 Andrew McCann
It's button? There we go.

38:51 Danelle Cline
That's the one.

38:53 Eric Hofesmann
No. Yeah. So yeah, it should be that Tilda key.

38:57 Laura Chrobak
Yeah, For me, for the tilda.

38:59 Danelle Cline
Yeah, I'm not, I'm not getting the tilda. I'm sorry. It's from the operator error. Tilda, the point of that is, is just like the last thing I just did.

39:11 Eric Hofesmann
No, yeah. So what that does, it basically does the same thing as just clicking on those three lines to open up the operator browser.

39:17 Danelle Cline
Oh, I see what you mean. Yep.

39:19 Eric Hofesmann
It just allows you to kind of do it through the keyboard so that you can hit tilda and then enter And then it'll Run. Ah-huh. The most recently used one.

39:26 Danelle Cline
I, so now If you hit enter, I figured it out. Okay. And then so, so Tilda no shift, I was shifting and then Ah, gotcha. Okay. Yeah, enter. Oh that's not like you can enter Enter. That's not so bad.

39:42 Laura Chrobak
Yeah.

39:43 Eric Hofesmann
And then you gotta kind of click this every time to select that label, but you Can type right.

39:50 Danelle Cline
That could, Yeah.

39:51 Eric Hofesmann
And you should be able to then hit like down on the arrow keys, hit enter, and then add the values.

39:58 Danelle Cline
Yeah. That's not too bad. It's workable.

40:01 Eric Hofesmann
Yeah. For the time being until we get this plugin together at least.

40:04 Danelle Cline
Yes.

40:04 Eric Hofesmann
It'll let you start working with this. Yes.

40:11 Laura Chrobak
So a few like follow ups to that step. Is there an idea of like snapshots or like let's say as our labelers are going through these and we want to say save a view, anything like that? Yes.

40:29 Eric Hofesmann
Yeah. So we probably should have done that before we started, before we actually made like this change. But we can do that now. If you go up where it says samples at the very top, if you click history, so this is exactly where you can create snapshots. So you can, let's try it now. Let's just say, you know, snapshot one. So this basically creates snapshots of your data set in time. So it kind of creates a read only version of this data set that you can then always go back to and view or you can roll back to a previous snapshot. That's cool if you want to like undo changes. So yeah, let's go and create that.

41:06 Laura Chrobak
Does it have to be manually done or can it be like automatically done at some cadence?

41:12 Eric Hofesmann
You can do it with Python code. So in theory you could have some like script that gets run automatically on your computer.

41:20 Danelle Cline
So help me, help me understand where this is used in practice.

41:25 Eric Hofesmann
Yeah, so it would be like as like maybe before an annotator comes in and makes any changes. Okay. Like if I'm about to start working with the dataset for the day. Okay. I would start by creating a snapshot of the dataset and then I would go in, make some changes and then when I'm done I would create another snapshot. So then you can see all of the changes that have happened in time. And if I accident make a mistake, I can roll back to a previous snapshot. So that's kind of the idea.

41:54 Danelle Cline
Oh Yeah, that's kind of cool. I like that. Yeah, that's helpful.

41:58 Laura Chrobak
Yeah. Remember how Danelle we were talking about the like change history?

42:02 Danelle Cline
Yeah.

42:03 Laura Chrobak
And so with our like existing data sets, we rely on this and in lieu of that here, I think that this is our avenue for making sure that we can go back to a state that we agree is Yeah, it's and it and it allows you to operate within the same data set the same output of the model, that kind of thing.

42:23 Danelle Cline
Yeah.

42:24 Eric Hofesmann
So can you click on like the, the three buttons next to browse for this new snapshot that you just created?

42:32 Danelle Cline
Oh, sorry, the Three button?

42:34 Eric Hofesmann
Yeah. So if you click browse, it brings you into like the view only version of that. So here is where you can then like roll back to a previous snapshot if you wanna undo changes. But importantly I just want to call out this clone to new data set. So if you don't wanna undo the changes but you wanna kind of keep working with data, you can then click that and it'll create a new data set with like the, a certain snapshot. So it'll still keep all the snapshots on this one, but you can then kind of like branch off and then do something different from that point in. That's Excellent.

43:04 Danelle Cline
Oh cool. Cool.

43:07 Laura Chrobak
Is there a concept of undo?

43:11 Eric Hofesmann
Not at the moment. Yeah.

43:13 Danelle Cline
Is there Undo is a tricky thing to, to code.

43:17 Eric Hofesmann
Yeah.

43:19 Laura Chrobak
Is there a ability to view what was recently changed?

43:26 Eric Hofesmann
Only kind of, can you go to samples and then can you actually click back to this, back to latest version in the top right. So right now we're in the snapshot view. So this brings us back to the live view. So down where it says last modified at every sample has this kind of time tracker for whenever a sample gets changed. So for example, if you update the label, then it will tell you when that last modified time is at. Yeah, exactly. So this should then show you might need to reverse the search. Yeah, it should be all the ones that we just changed through that.

44:07 Laura Chrobak
Yeah, that's great.

44:09 Eric Hofesmann
One thing that could be interesting, can you click the plus next to samples and then open up the histograms panel. And then can you open this last modified at scroll down, curious what this looks like? Yeah. So you can kind of see like when some changes happened. So we see that there was 52 samples that were changed at this time. So this could be a way to kind of see some Information.

44:34 Danelle Cline
Yeah, we started with 9,000.

44:37 Laura Chrobak
We just, How did you get to the histogram?

44:41 Danelle Cline
Okay, we'll do it again. I did plus and then I did histograms.

44:45 Laura Chrobak
Cool, Thank you.

44:47 Danelle Cline
And then selected. And that can be, I like this view 'cause it's if you have whatever your tags might be. Yeah.

44:56 Eric Hofesmann
Can you actually do ground truth thought label? That could be interesting too. See the distribution of different labels you've got. In fact this is kind of a deprecated version of this. We do have a fancier, newer version of this Instagram.

45:07 Danelle Cline
Oh Nice.

45:08 Eric Hofesmann
That makes be interactive as well. Oh that's very useful.

45:11 Danelle Cline
Because that's the first thing I did when I, when I opened this, I'm like, why can't I go drill down?

45:16 Eric Hofesmann
Yep.

45:16 Danelle Cline
Thing. And it and it's because, and it, or you know, some of these things are really interesting too to like, our tail can will get longer. 'cause that's just the nature of natural data as I'm sure you know. And, and some of these things are seen very rarely or seasonally.

45:33 Eric Hofesmann
And Yeah, those are probably the most interesting ones.

45:37 Danelle Cline
It can be, it depends, it depends on the research question. Sometimes they're really interested in, some of the scientists are really, they really interested in sort of grouping some of these broader kind of classes together just to know maybe three main groups. And some are interested in rare things because they might indicate, you know, it, it's all very driven by the science. So flexibility's key I think for us, I think at the end of the day we're really just, we still need to have the data curated by the experts at to the lowest taxonomic levels.

46:23 Laura Chrobak
Okay.

46:23 Danelle Cline
So, So let's get out of this.

46:26 Laura Chrobak
I have two additional questions that might take like 10 minutes. Is that fine? Sure.

46:37 Praveen Palem
Just before we move on to that though, I, I just wanna quickly ask if you're interested in the in tool founding box, sort of like annotation features Danelle or is that not It's simply labeled.

46:49 Danelle Cline
Not at this time, but, but maybe next time we can touch on that. I, okay, I have a meeting in 15 minutes and I have a question before I, this is a newbie question I'm sure, but I have to ask it because this meeting is to talk about this tool with another researcher. I have the community version and I'm able to load data and it all works beautifully in terms of the Python part. I can, I have a separate Mongo database. I've spun up in a docker container and I'm running the community version and that all works. So we're evaluating it for her dataset, but I can't get the session to connect. I keep getting session timeouts, but the data's there, it's in the database, it's connected. And I am out of ideas on why I can't connect to this session. I've tried rebooting the machine. That doesn't help.

47:56 Eric Hofesmann
So what's, what's going on with session inability to connect That is often like networking weirdness of the machine Really Putting it on. So I have question, is there a reason why you can't load that data set into here?

48:16 Danelle Cline
This would allow you just kind of Oh yes, I had thought about that. Yes I could, but I, you know, it's, it's not technically for her project.

48:29 Eric Hofesmann
Ah, okay.

48:30 Danelle Cline
But I may need to because I can't get it to work and we have a time critical deadline to finish this before the end of the year, so. Yeah. But I, I hear you. 'cause it was working yesterday and now it's not.

48:49 Eric Hofesmann
Oh, interesting.

48:50 Danelle Cline
Okay. Yeah, so I don't, I don't know if something's changed because I'm not, I don't maintain these systems I'm working on and if there was a patch that was done or do I, if I need to disable like the firewall and I probably shouldn't do that, stuff like that. But there's nothing like naive about the session connection.

49:18 Eric Hofesmann
Yeah, it's usually I, the, I mean really the one thing that trips some people up is if there is already a running session that can cause some issues.

49:27 Danelle Cline
So How do you know if there's already a running session?

49:30 Eric Hofesmann
It's really like check the running processes on your machine, just do like a through H top or something and then see if there's already a 51 Python session running and if there is, kill it, like kill all the 51 Python sessions and then try launching like, you know, starting it up again and launching the app. That's kind of the one kind of easy thing that trips a lot of people up and Yeah, I'm not giving machine just to Sort of Okay, yeah, then that'll do it.

49:57 Danelle Cline
Yeah, and that didn't help. So something has changed and I can't quite put my finger on it, so. Okay. Well I had to ask because it's a time critical thing to, to try to go through this. So if I can't get it to, if I can't figure it out, I'm just, I'm just gonna load the data into this Juul That Yeah, that would probably be, I mean that's definitely like the guaranteed thing and we can also send you what that looks like.

50:21 Eric Hofesmann
It's like two lines of code to kind of dump it from the Mongo and open source and load it into the enter.

50:26 Danelle Cline
Oh really? Yeah, the data needs to be in our, our cloud bucket though, right? There's Yes.

50:32 Eric Hofesmann
Okay. Three lines of code. So move the data, the data set and then upload it to the cloud.

50:37 Danelle Cline
That could be useful to know actually.

50:40 Eric Hofesmann
Yeah.

50:40 Danelle Cline
So I'm gonna, I'm gonna jump now so I can try to work on a little bit more before my meeting with her and I'll Catch up.

50:49 Eric Hofesmann
Yeah. And also if you can share just like the session error that you're getting in Slack, we can also take a look at it just to see if it Something, it says timeout.

50:55 Danelle Cline
It just says timeout. I'm starting again in 10, 10 seconds. Timeout. I can't, Oh, It just keeps timing out.

51:03 Eric Hofesmann
It, it creates a data set, it populates it and, And when you try and load up the local S app, it doesn't show anything in the browser.

51:17 Danelle Cline
Yeah. The browser opens up and it says you don't have any data sets.

51:21 Eric Hofesmann
Here's how you create one And then if you click the dropdown in that, in the 51 app, Oh, That might be the thing.

51:30 Andrew McCann
Like this actually I gotta Take off guys.

51:33 Eric Hofesmann
I'll see you next time.

51:34 Danelle Cline
Yeah, No, it wasn't there, but I'll, I'll keep trying. I'm sure it's some newbie thing, but it didn't, it didn't show up immediately, but, and I wanted to make sure like my versions were all synced up on both client and, and the server. So there's something that I, it, it could very well be something that I did too to set up the environment that's different that I can't remember, but I, it it's all, it's all really, really straightforward.

52:06 Eric Hofesmann
There's not a lot of Yeah, and not that you mentioned it so that specific like session or like, you know, server is timing out that is not often an actual error that's kind of like just a warning that it's throwing and Okay's A good chance that it may be working okay. But it might be like connecting to the wrong session or something, so.

52:26 Danelle Cline
Okay.

52:26 Eric Hofesmann
Okay.

52:27 Danelle Cline
Just think I need to be more patient.

52:30 Eric Hofesmann
I think I might have seen that.

52:33 Danelle Cline
Well I will stop sharing. Let's see, go back here. Stop sharing. Thank you so much for your help everyone. It's, it's been terrific and I'll leave you with Laura, have a great time.

52:48 Eric Hofesmann
Laura, It's great meeting to get Danielle.

52:51 Praveen Palem
Yeah, we don't find staying a, a few extra minutes but Danelle, so next week is Christmas weekend and then Yes, the following this New Year's weekend. So are we meeting in the new year or?

53:02 Danelle Cline
I think the new year is safe. Okay. And of course we can reach, reach out if we have questions on Slack.

53:06 Praveen Palem
Anytime.

53:07 Danelle Cline
Anytime Because it gets pretty quiet here and I think, is that okay? Laura, are you in January?

53:14 Laura Chrobak
It seems like a reasonable next time.

53:16 Danelle Cline
Yeah, sounds good. Okay.

53:18 Praveen Palem
All right. Yeah, yeah, I mean feel free to ping us on Slack, but either way, have a lovely holidays and you know, Merry Christmas.

53:26 Danelle Cline
Oh, same to you Eric. Pravin, Laura, bye.

53:30 Eric Hofesmann
Happy holidays.

53:33 Praveen Palem
Alright, Laura, then there Were three.

53:37 Eric Hofesmann
Yes. Okay, cool.

53:39 Laura Chrobak
The, the other two things that came up to my mind we're one around our label maps and how we might keep track of that. Right now we have currently two sets. One is the ground, the one that we wanna move forward with and one is kind of a deprecated set. And I'm wondering is there a mechanism to keep track of different label sets?

54:16 Eric Hofesmann
Mm. So this is all for the same sample, like the same images, you just have different label sets for them or there, is there also discretion?

54:24 Laura Chrobak
No, they're different data sets. And so essentially what I, for for example, I have, let's say I have two, one with map one, one with map two, I would like some of our reviewers to look at the data set number two and remap things to what the classes are in map one. And obviously we could just have a long list where they're all combined, but it's a little bit confusing for somebody to mentally know which ones are considered acceptable and which ones aren't. So for instance, when we upload that dataset number two, maybe Voxel 51 will have a history of our previous labels from the first set and it will also now know all the new labels, but I specifically do not want the ones that are in the second dataset to be co like to be used further on. So that's kind of the problem is ensuring that if you're ever remapping, it's to that specific set. So for instance, in this plugin, I would like it that the label options are only from one specific label map, so that you could never change it to anything other than those options.

55:51 Eric Hofesmann
Hmm. Yeah, I mean, just off the bat what I'm thinking is probably have all of this in one data set, so have all of like the samples that spans everything have one label field of like the label map too. And then another field with the first label map. And then you can actually set fields as read only so you can make it so that like those initial labels is a read-only field that people can just use as a reference for when they're kind of updating the new labels. And then I believe even the plugin that we've looked at today with the edit field values, I think that is also scoped to just the single label field that you're editing. So when you select ground truth labels, then the available classes to choose from are only ones from that field. You can't actually choose ones from the other. So I think that may actually just kind of work out of the box and then definitely we'll make sure for this other plugin to also have that behavior.

56:47 Laura Chrobak
Would you be able to filter for, for instance, like, so there are certain classes in this second dataset that I want changed, but the majority of them are fine. So I could populate field one and field two kind of programmatically, but for field two I could withhold a label if it's the one that I want. Oh, if I, if it's the one that I want changed. I guess the, the thing here is that some of, some of the classes are, they're like, they're hierarchical and so it's that we're, we're, we have nested ones. Maybe I need to think about this question a little bit further before, but I understand that there are label like set fields, so that's helpful. And potentially next week or the next time we meet, I might have some specificity in the plugin for what we're allowed to set.

57:55 Eric Hofesmann
Yeah, no, I think I can think about that a bit more. The hierarchy definitely makes it a little trickier. One way that I've seen that done is like you have that classification per sample, right? Where you've got the label with some class you can then have other custom attributes on that classification.

58:10 Laura Chrobak
Yeah.

58:10 Eric Hofesmann
So you can then have like super category or like, you know, some kind of hierarchy that way.

58:16 Laura Chrobak
And then yeah, we definitely Would like, how do you do that? Like could we, so we have a very easy map that shows for each of these names it maps to a super category. Is there an easy way to fill that in?

58:30 Eric Hofesmann
Yeah, so that's just easily done in Python. So like whatever code that you have to ingest the classifications, whenever you create the 51 classification label, it usually looks something like, you know, FO classification with a label. You can then add whatever other custom attributes. I'm just gonna type it in this chat real quick, quick class. Okay.

58:51 Laura Chrobak
So it would be added as an attribute?

58:53 Eric Hofesmann
Yeah.

58:57 Laura Chrobak
Okay.

58:58 Eric Hofesmann
So something like this where like the label is what you provide and, but you can have any arbitrary custom attributes for each classification that you create. And this would be then on one of the fields of your sample.

59:17 Laura Chrobak
Cool. Can you use the histogram to look at attributes as well?

59:22 Eric Hofesmann
Yes. Yep. And you can filter by them and all that good stuff.

59:27 Laura Chrobak
Sweet. Okay, that sounds great. I think The next, next week I think our, our near term goal is to really bring in that initial data set so that we can get our partner to kind of review those. And one thing that I'm wanting is to have one for, for us to be able to compare the initial view with the one that he's editing. So I, I think that having just a quick discussion set up about that would be helpful, but we can tackle that in the new year. So thanks so much for your time, I really appreciate it and I'm excited to dive into this. I, I was totally out this past week, so I haven't had the opportunity, but it'll be fun.

1:00:26 Praveen Palem
Yeah, no worries. Glad you're feeling better. And thank you for your time and we'll talk again in the new year and of course ping us anytime you're still working next week, you know, I'll be glad to answer any questions.

1:00:39 Laura Chrobak
Cool. I won't be around, I'll put stuff in there, but there's no need to respond to it at any fast cadence over the holidays.

1:00:50 Eric Hofesmann
Awesome. No worries. But yeah, it's great meeting you Laura.

1:00:53 Praveen Palem
Super cool stuff.

1:00:54 Eric Hofesmann
Yeah, Yeah.

1:00:56 Laura Chrobak
Should be fun. Figure out these phytoplankton.

1:00:59 Eric Hofesmann
I know, Right?

1:01:00 Praveen Palem
Are these, are these all phyto franks or a zooplankton as well?

1:01:04 Laura Chrobak
Great question. So there are two magnifications, and this is the higher mag data. And so this is phytoplankton because they're small. The low mag data is going to probably have a combination of those things because Yeah, it's like looking at a, a different range of sizes, but Gotcha. As far as I'm aware. Yeah, that's good to know.

1:01:32 Praveen Palem
I'm, I'm just learning what Planktons asking.

1:01:35 Laura Chrobak
Yeah, the, the low data, which you'll probably see some of Denelle's working with Colleen's team on that. And that gets really tricky because you start to get like a lot of aggregates and Yeah. Like not distinguishable organisms. So that gets a little trickier.

1:01:55 Praveen Palem
Oh well Planktons, my new favorite SpongeBob character.
