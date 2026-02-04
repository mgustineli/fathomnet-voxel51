## 2026-01-15 - MBARI Sync

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/d26b1f4a-39ad-4c60-997a-66ad1a036086

**Voxel 51 Participants:**

- Praveen Palem
- Sid Mehta

**MBARI Participants:**

- Laura Chrobak
- Danelle Cline

**Meeting Notes:**

- Presented updated bulk edit plugin with configurability: current view vs selected samples, excluding selections for large datasets
- Demonstrated plugin on embeddings view (works with lasso selection + sample IDs, not just label filters)
- Discussed label field selection: defaulting to "ground_truth" with option to make it user-selectable
- Covered verification workflow challenges: need to track reviewed vs unreviewed labels, discussed using separate fields vs tags
- Planned workflow: prediction field → bulk review → populate ground_truth field when verified
- Discussed constraining label changes to dropdown (prevent typos) vs free-text input
- Introduced MCP server for AI-assisted plugin development in IDE (Claude/Cursor integration)
- Covered local plugin development workflow for enterprise (debug mode vs production deployment)
- Set timeline goals: complete model iteration by spring experiments (multiple deployments needed for high/low mag cameras)
- Action items: finalize plugin with ground_truth default, send plugin code, schedule Patrick for label review, migrate OSS data to Enterprise

### Transcript

01:04 Praveen Palem
Hey. Hey, Sid.

01:06 Sid Mehta
Hello.

01:07 Praveen Palem
Can you hear me okay?

01:10 Sid Mehta
Yes.

01:46 Praveen Palem
Hey, Laura.

01:47 Laura Chrobak
Hey, how's it going?

01:50 Praveen Palem
Good. How about yourself?

01:52 Laura Chrobak
Great.

01:53 Sid Mehta
I think now your voice is a little faint. Pravin.

01:57 Laura Chrobak
Oh, really?

01:59 Praveen Palem
Okay. Let me, lemme check Mine.

02:03 Sid Mehta
No, Pravin.

02:08 Praveen Palem
Is it still faint?

02:09 Sid Mehta
Yeah.

02:10 Praveen Palem
Okay. How about now?

02:29 Sid Mehta
It's a little better.

02:32 Praveen Palem
One second.

02:36 Laura Chrobak
Hey, can you confirm it's okay now It's a little faint, but we can't not hear you.

02:43 Praveen Palem
Okay. One second. Yeah, I don't know what's going. I okay now.

03:34 Laura Chrobak
Sure.

03:34 Sid Mehta
Kind of still the same.

03:44 Praveen Palem
All right, let's give Danelle one more minute maybe, and we can How are your third stays? I'm sorry, say again?

04:16 Laura Chrobak
How was your Thursday going?

04:18 Praveen Palem
Good, good. Just staying busy. How about yours?

04:25 Laura Chrobak
Pretty good. Welcome.

04:27 Danelle Cline
Hi. Sorry I'm a little late.

04:34 Praveen Palem
Okay, so where should we get started? Let me review the notes that we, that, that I sent in Slack and then we can, we can tackle one, one item at a time. Okay. So first, the, the main update from me is the, the, the, the plugin that I showed you Now, I kind of changed it to where it kind of does what you intend to do, Laura. At the same time, keeping in, in, in consideration the fact that if you have a large data set and you try to select all of them, then it could cause performance issues. So what, what we discussing with the product team, we, we came to a solution where you would actually select the negative samples that you don't want to change. And the plugin can change all of the images in the view except for those. Does that make sense?

05:46 Laura Chrobak
To select the negative ones that you don't wanna change. So the ones you wanna keep and Yeah.

05:53 Sid Mehta
So like let's say you add a hundred samples, right? And then, and this view, and you're like, I wanna change all of these except for these five. So then now instead of selecting all and then deselecting, you would just select all and it'd be, the plugin can be where it can be like, okay, these, these five don't do, but the rest 95 do. Does that make sense?

06:11 Laura Chrobak
Yes, it does make sense. Let's look at it.

06:16 Praveen Palem
Yeah, Yeah, yeah, yeah. It's easier to show, show it, I guess. So, so you might recognize this dataset path net, right?

06:24 Laura Chrobak
Yeah.

06:26 Praveen Palem
So the, I just uploaded this and then have this, the updated version of my, of my plugin. Don't go by the, don't go by the labels there. It, it's not a very good model. So just random label labels. Most, I think it's 50%, right? But, so let's say I want to edit. Let's take a, let's, let's start simple, right? So we'll, we'll take a simple label. I'm gonna take say centipede. I don't know, something that has more than one tighten. Yeah, Let's, let's take something bigger.

07:10 Danelle Cline
Try fish.

07:13 Praveen Palem
Oh, there's, there's no fish.

07:16 Danelle Cline
No Fish. Okay.

07:20 Praveen Palem
Wait, I thought I saw alligator. Hang on, hang on. Okay. Oh, starfish, You, I, I, I, I think I remember seeing something big. I mean one with a lot of things, but I might, I might have messed it up by playing around with it.

07:41 Danelle Cline
Try Sea urchin. Sea urchin.

07:48 Praveen Palem
Okay, thank you. Alright, so let's say I want to change all of these except for this guy, which doesn't look like it. Well it is cion. But anyway, so we'll, we'll say edit predictions two and then I'll say, do I want to change the current view or select samples only in this case? Because assuming this has hundreds of samples and not just kind of them, we are gonna say current view and I'm gonna exclude the one that I selected, right? And then I would select a new label and let's just say centipede, right? And then I would execute. And then it says eight samples have been now modified to centipede. Right? So now if I go to sea urchin, oh no, it's the wrong one. I would have only one.

08:50 Laura Chrobak
Okay, that's great. What if we wanna change just this one?

08:55 Danelle Cline
One.

08:55 Praveen Palem
Just this one? Yeah. So I did predictions again and instead of current view, oh, I mean in this case it's just one sample, so it doesn't really matter. But I would do selected samples only and then Centipede again and then done.

09:16 Laura Chrobak
So last time, yeah, when you went into the plugin, you did everything.

09:22 Praveen Palem
I selected samples only Everything except for the selected samples. I mean the first time, the second time I did selected samples only.

09:31 Laura Chrobak
Okay, so it's kind of configurable. You can do it either way.

09:33 Sid Mehta
Yeah, that's perfect.

09:35 Laura Chrobak
That's just what we need.

09:37 Sid Mehta
Awesome. There we go.

09:41 Danelle Cline
So, so after we make the changes, the query resets, so the view resets and that's by design, right?

09:50 Praveen Palem
Yeah. It's kind of inconvenient, but yeah, that's it. It it's by design.

09:54 Sid Mehta
Yeah.

09:55 Danelle Cline
But you Can't make a plugin change the view. So when you say execute, I can't reflect that.

10:03 Sid Mehta
So like what's happening is like, 'cause Pravin is using the sidebar filters to filter, right? So it's saying like all the labels that match this label show that, right? If you change those labels, those won't, that that that condition doesn't exist anymore, right? So it's there.

10:22 Danelle Cline
Yeah.

10:22 Sid Mehta
So that that's why it, it kind of like auto updates and like Yeah, also like one thing. So Pravin if you go to like unsa you, so yeah, I guess we maybe don't do a good job of showing this. I mean you can kind of see it on the side, but if you do like save view current us filters like our, like if you were actually to save this view, you would see that there's actually like the view bar doesn't populate up, but there are like filters on this view, right? So anytime samples don't fit that view or base those, those filters it, it should update to For that.

10:53 Laura Chrobak
So I was kind of imagining this workflow to be parallel with the embedding view rather than necessarily going by label and the filter. 'cause I was playing around with it yesterday and so I was thinking to know rather than having for instance Patrick go through make a view filter for class one and then use the plugin to make the changes that they would have the embedding side by side.

11:22 Sid Mehta
Yeah. So I think Pravin, if you do this with embeddings, it's still should work. So when you're doing embeddings, it is doing a view filter. 'cause what it's doing, if I'm not mistaken, is that you're selecting like lasso points and it's using a view filter called select IDs, right? So we have the like select samples. So it should be able to work with the plugins as well. So he's running it in embedding spot. But yeah, like that, like when you are lassoing these sample points, that is also like filtering out the samples, right? 'cause you're saying only look at those. So it should be able to still work in that case. But yeah, that's a, that's a good point. We can also double check and make sure that the plugin works as expected because Yeah.

12:00 Laura Chrobak
Yeah that makes sense.

12:01 Sid Mehta
'cause that's the mode that you're gonna be when you wanna bulk edit it.

12:04 Laura Chrobak
Yeah, let's try it out. I'm curious, like I'm curious, for instance, let's say I circled a cluster and then I'm looking at the grid on the left and I use the plugin and then once it updates, am I still looking at the residuals of what was in the cluster or what's that next?

12:24 Sid Mehta
Yeah, you should be able to see the residuals because at the end day that filter was based on you just selecting the samples based on under the hood their sample id. Right? So you changing the filters, you changing their, the bulk added the label shouldn't affect what goes on because you're doing a, because here you were defining the filters based on the label and because you changed the labels, that's why there was a change. Whereas like and the workflow that I think what's gonna happen is that like Yeah. Do you have like a Yeah.

12:53 Praveen Palem
Green key? Yeah.

12:54 Sid Mehta
Perfect.

12:55 Praveen Palem
So This is just a hundred of them, but I think it should, it should be fine.

12:59 Sid Mehta
Yeah. And do you wanna color by like class classification label?

13:03 Praveen Palem
Yeah. Got it.

13:05 Sid Mehta
Yeah. So let's take this one. Not the best cluster in the world, but like it is what it is. So yeah, let's go to like that one. So yeah, like you see three images here and Yeah, if we run the plugin.

13:19 Praveen Palem
Oh, this one? Yeah. Hang on. I might not have predictions. Not a classification.

13:28 Sid Mehta
Oh is it not a classification field?

13:31 Laura Chrobak
Yeah, It's like a, A detection set.

13:35 Praveen Palem
Yeah, I think it should be, this is a detection set I think once, yeah, I guess the question is why is it defaulting on the Yeah, that's, that's just the, the plugin just to use looks for the predictions field. I could change it to. Okay. Any random? Yeah, like maybe, yeah, select Any, any.

13:54 Sid Mehta
Oh okay. I think I got it. Yeah, so I think like what we might wanna do in a plugin is that they can select what type of label field at the beginning that they want bulk label as well. 'cause they might have, I don't know, do you get into that case lower in know where you might have multiple labels per Yes. Sample?

14:09 Danelle Cline
Yes. We could have, in some of our processing we use, we have a label and a label S, which is like the second got two, top one and two.

14:18 Sid Mehta
Yeah. Yeah. So that's like one thing. Let's see if on this one, but I think this one, it also might be a classification.

14:26 Danelle Cline
It might be also bad being run the same error Because the ground truth has a special meaning in this. I think we want our default to be the ground truth label.

14:35 Sid Mehta
Okay.

14:36 Danelle Cline
That's ultimately what we're revising.

14:41 Praveen Palem
Okay, got it.

14:42 Laura Chrobak
Yeah.

14:42 Danelle Cline
In the sense of voxel. And do I got that right?

14:45 Laura Chrobak
Do I have that right? No, I was just thinking ideally ground truth is reserved for something that we feel is very verified versus like for instance in this, you could imagine us doing this workflow where we've run our model over everything to get the class prediction. But that's just a start. That's a label starting point and I think that that metadata field should be reserved for something that is human verified.

15:14 Sid Mehta
Okay. So yeah, I think what probably the best solution is for Pravin when we like maybe to just to add like a, a label selector dropdown to the plugin so they can select like this is the label.

15:24 Laura Chrobak
Yeah.

15:25 Sid Mehta
That I wanna work with. I want to, but it might not like, 'cause you know, you probably want the flexibility and Yeah, I guess like right now it's probably good that you're only looking for classification labels at the moment. 'cause I think that's what you guys mainly work with, right? You don't lower or do you guys work with bounding box at the moment?

15:39 Laura Chrobak
No, not for this project.

15:40 Sid Mehta
Okay. Yeah. Yeah. So I think it's fine that it's only looking for classification labels. But yeah, I think that's like if Pravin has that then I think that would, that would make it so it's a bit more flexible. It can like I think we can get it to where it shows all the classification label fields and you can select, okay, this is the label field, I wanna bulk edit and then you go into make things a change.

15:58 Praveen Palem
Okay. Yeah, I, I can make that change real quick and then send it over to you Laura and then I can also walk you through just installing it and I would love for you to start playing around with it.

16:06 Danelle Cline
Yeah, that'd be awesome.

16:08 Laura Chrobak
I'm thinking, okay, so there's one more thing that would be such a nice to have in this plugin and I don't imagine it would be too much of a stretch, but all right, imagine that you have this cluster, it's got a hundred urchins in it, you change 10 of them to be a different class. Now that that, let's say that other class is fish. When you go to the fish cluster, you have a bunch of labels that the model had predicted, but then 10 of those you have verified, right? Like you change and that label is now human reviewed in a sense. And so we don't want, for instance, our labelers to have to re regard that, those 10. So if we could possibly put in a label when you change, or sorry, a tag when you, when you make this plugin change that says verified or reviewed or something like that. That way when they go to the next cluster, they could add an additional filter that says, you know, like doesn't have this tag. Ah, then they're only looking at the queue of things that like haven't been updated that that's my like initial implementation. But I'm just, I, I would be open to brainstorming. I'm just thinking of a way that Patrick doesn't have to do double work in that scenario.

17:41 Sid Mehta
So that No, that's an interesting point. I think, so one thing I will say between tags and like let's say like a label field, right? Because you could also have a label field, let's call this like verification, right? And what are the statuses? This could be, this could be verified or review, right? Those are the only two.

17:57 Laura Chrobak
Yeah, it's, it's, it would either be verified or unverified.

18:01 Danelle Cline
Yeah. Right. So Verified in our current system is a Boolean and okay, it's an attribute.

18:06 Sid Mehta
Yeah. Yeah. So what I would recommend like as a step is that one I would add a, because what I like about label field versus tags, tags, you can have, you can have two tags at once. So to avoid getting to the state where you can have an unverified and verified tag, it's like well what do we do? Right? So like, because then you also have to worry about deleting tags. Whereas I think that's why like the data structure of just having a label field, because in label field is you can only be at one state at a time.

18:31 Laura Chrobak
Right? Okay. So I I I see that but in the scenario that I described, you had your urchins, yeah, you changed 10 of those. But by nature of not changing the remaining 90, you've actually approved those, right? Like you've looked through them, you've said these are all actually urchins. But now that would, I also have to update that, you know, that label would now need to change to the new label you're talking about.

18:56 Sid Mehta
Okay. Wait, so I'm, I'm a little confused. So like in the example, like is this, so, okay, so you have like a hundred C urchins and you're saying how many of them you want to approve as like how many of them do you want to change the label to be Nazi Urchins?

19:10 Laura Chrobak
10 of them aren't sea urchins, 10 of them are fish. And so you've gone in and you used to plug in to update the new LA named fish. And in your method you're suggesting that the late, basically the label change to like verified label is now fish. But when I'm querying my whole set, all of the urchins never got updated. And so they're, they don't have that new field in there.

19:36 Praveen Palem
One again, let me clarify. So we can have two label fields. One of them is the actual classification and I, I think if I'm not mistaken city saying you can have a second one that simply has two that has verified and unverified in it.

19:48 Danelle Cline
Correct.

19:49 Praveen Palem
And then what you would do is after you change the sea, 10 of the sea urchins to fish, then you would filter by sea urchins and then put this label on let's says it's verify, right?

20:03 Sid Mehta
Yeah.

20:04 Laura Chrobak
Yeah.

20:04 Sid Mehta
So I guess my question is which of like the 90 that you change that you didn't change to urchin or the 10 of the fish, which ones should be, should have the new verify tag.

20:14 Laura Chrobak
So be like in that cluster, all of them have been reviewed, right? You have gone through and you've looked through all of the urchins and you've looked through the fish you but you only modified one of them. But I still need a way to communicate that this set is Okay Done.

20:33 Sid Mehta
Yeah, yeah. That should be possible. Pravin. 'cause that that's basically saying at the end of that operation, regardless of whether the label field changed or whatnot, it's verified because anything that's selected in this ID or view. So yeah, I think that's like the thing. So in that case, like the operation needs to happen on all a hundred samples regardless of 90 10.

20:50 Laura Chrobak
Okay, So that was, sorry that that was to introduce this issue. But now let's say you have two classes that you need to change. You make the first change to fish and there are still three or three additional ones that need to be updated. But those aren't verified urchins, right? Like you have your a hundred urchins, 10 are fish and 10 are actually sea stars. And so I need to make two changes. I need to update the label on the fish and I need to update the label on the sea star. If it applies the verification to the whole set, then we've got an error with that second class. So essentially, I mean I think that you, you don't have a provisions for like some type of Boolean state that you can set in the metadata.

21:41 Danelle Cline
Well I Just interject here. It seems, it seems to me that that a label going, a label going from a label to the ground truth is really that verification process and that the verify flag in this scenario is a is kind of redundant.

22:02 Laura Chrobak
So Yeah, I agree with you.

22:05 Danelle Cline
But then, So let's say we both edit the label. When you go in and edit the label, the labels are there, they're machine generated and then the user says, okay, now the ground truth exists and we know it got updated, we know the timestamp, it got updated. Yeah We could use that information and then sort of abandon this idea of verified or not.

22:27 Laura Chrobak
Well Danelle, the ones that I'm, the case that I'm talking about is the ones that the machine got correctly. So if the machine predicts it correctly, you don't update the label but it's still been reviewed and so we need a way to Gotcha.

22:39 Danelle Cline
Okay.

22:40 Laura Chrobak
Keep that. Those ones are good. Even though you, like we could have, we could make Patrick just, ooh that's an idea. I mean it would be an extra step but I think this might work. So you made your fish change, right? And now that goes to the new field ground truth. And then you do the same for everything in urchin, but you're populating the new field rather than, or you have to populate the new field. So you had a hundred urchins.

23:15 Praveen Palem
So for the 90 of them you would go and say verified You would go in.

23:19 Laura Chrobak
Well I think that you would go in and based on our idea of populating the ground truth field, which is was originally empty, you go in and say everything remaining gets, it's now this label the same label but in the field called ground truth.

23:37 Praveen Palem
What, what, what's the, what's the first field if, if the second field is ground field, what would you call the horse field?

23:43 Laura Chrobak
Just like label one Prediction.

23:45 Praveen Palem
Okay.

23:46 Laura Chrobak
Yeah, prediction.

23:47 Praveen Palem
Okay. Okay, got it.

23:51 Laura Chrobak
Does that make sense to people?

23:54 Sid Mehta
Kind of, I feel like we might need to see this one might we need to bake out a bit more? It might need to see like I think what would be maybe be helpful is that Pravin if we give them like this version two where you have the, you select the label, like let's get this one to where it it is for them. And then I guess like l Laura, it'd be nice if we could like then use that plugin and kind of see like what it was. Sure. And I feel like it would make a lot more sense.

24:13 Laura Chrobak
Sure.

24:13 Sid Mehta
So maybe let's work towards that goal. 'cause then like yeah, I, yeah, I'm like, now I'm like 90, now I'm like trying to remember which phishes we turn into see or and whatnot. So it's, it's like easier. So I think Pravin, if we like focus on like the getting like this one, I think we're very close anyway. So we focus on this. I think once you send them Pravin, I think lo Laura we are, and we already showed you how to like install those plugins, right? It's the same thing. The zip zip thing. So we just wanna verify that you can install work the plugin on yours. So it should be like super easy. But I think like if you get around and play with with it and then we can kind of show you what's this like verification use case we, we can 'cause like the whole like valve thing that I was shoveling. So I guess there's like two things, right? One is like the bulk editing, which I think vin's thing solves. But then this verification is like another interesting thing.

24:55 Laura Chrobak
Yeah.

24:56 Sid Mehta
And that's like something that our like auto labeling panel that I was talking about, that's what that's for. Which is like approving and rejecting labels but it doesn't really solve the bulk editing piece. Right? So I'm, I'm trying to think how we piece together, right? If we can work both. 'cause the, 'cause the approving and rejecting labels is something that you can kind of do in that panel. As I as I It's true. That's true.

25:15 Laura Chrobak
I agree with that. That, that makes total sense. I think this idea of taking it step by step is valuable. Let's work with this plugin as it is and see if we do need to introduce something else.

25:30 Sid Mehta
Hmm. Perfect. Cool.

25:32 Praveen Palem
Awesome.

25:32 Sid Mehta
Yeah, so I think, yeah Pravin, I guess once you, I guess take some of the feedback that they have and you just send it to them, it should be pretty quick for you guys to just, you know, zip it and then just install it on the plugin. I think you both are admins, right? So either of you can do it and then you should just see it, right? Right. Where Pravin has it in the modal as well. So it's super easy and findable. And then also at like some point we can also talk to you and maybe show you like how you could develop and like edit these plugins locally easy.

25:58 Laura Chrobak
Yeah.

25:58 Sid Mehta
So you can also test some of this stuff. So we can maybe walk through that in like a in the next call.

26:04 Danelle Cline
I think that would be great.

26:05 Sid Mehta
Yeah. But no, I'm glad it's, I think there's a bulk, we were talking about it in our like sinks, but yeah we were talking about like bulk annotation and yeah this is all the more reason to invest more on it. So yeah, I think this is really good feedback from you guys.

26:20 Laura Chrobak
Cool. So did you wanna walk through adding the plugin now?

26:27 Danelle Cline
Yeah, yeah.

26:29 Sid Mehta
I guess Pravin, if you want to send in the one that you currently have, I know you're gonna make changes, but if you just wanna like just so they can practice.

26:37 Praveen Palem
Yeah, the only thing is it, it looks for a field label called predictions.

26:42 Sid Mehta
Oh okay. Yeah. Yeah.

26:46 Laura Chrobak
Can we really it, would it be easy enough for you to just change that field?

26:50 Sid Mehta
I can give you the field that we're currently using or like, I guess, yeah, did we install some plugins already on yours? I guess Laura, it'd be, it'd be the same thing. I can maybe walk you through, I think we did it with Danelle the first Time.

27:02 Danelle Cline
Yeah, it's super simple. I don't, I don't know. And Laura, it's just uploading a zip file.

27:06 Sid Mehta
It all you have to do is simple. Yeah. Yeah. Pravin will just send you the zip file and then all you have to do is just compress it and then upload it to, if you go to the your settings page. So if you see lc and then you click that and then if we go to plugins, yeah, so then install a plugin and then it gives you this, it's literally just a drag and drop. So that's all you need to do. Right?

27:32 Laura Chrobak
But can I change the field that it operates on rather than changing the dataset field?

27:40 Sid Mehta
Say that again? So what do you mean by that?

27:44 Laura Chrobak
Our labels are all currently on the ground truth field. And I think Pravin was saying that the plugin operates on another field.

27:53 Praveen Palem
Yeah, yeah. So what I'm gonna do is like we discussed, I'm gonna make it configurable where you can actually select the label that you want to edit.

28:02 Sid Mehta
Yeah, yeah, yeah. So you can configure it. So based on your dataset it'll look and see like, oh these are the label fields I have and then you can make it a dropdown. So that way also I think we'll hand you like a plugin where this is like a good one to build off of as well so you can kind of see the different components. 'cause then you know, the idea here is that you're not reliant on us to build these, you can kind of take this and edit it yourself. So I think what's, if you let Pravin just like, I'm sure he can knock it out pretty like I'm not gonna speak for it, but like I'm sure he can get it to you guys relatively soon so he can edit it. It's not the biggest change.

28:29 Danelle Cline
And then like I think it's be able kind of Use it default for that. Right? So our, most of our workflows use label. We would just set that as a default in the dropdown.

28:39 Sid Mehta
Got it. Yeah, yeah, yeah. We'll make it so you guys can choose. So it'll just be like, here are the label fields and you wanna do that. If you can also set a default option, we can, we can show you how to change that. That might be like a good for small change to do on your plugin. But yeah, I think we'll probably do something.

28:51 Danelle Cline
Yeah, I think the goal here is make it as the human computer interaction has minimal minimize the clicks. Right?

29:00 Praveen Palem
Yeah, that's a good point. So, so you know there's a trade off between configurability and Yes. Making foolproof.

29:07 Danelle Cline
Yes.

29:07 Praveen Palem
Yes. That's why we're trying to draw the line, I mean a balance. So I guess what Elli is saying is make it default to a label called Ground tooth. Is that, is that right?

29:16 Danelle Cline
Yeah, exactly.

29:18 Praveen Palem
Okay. And then would, would you want the the user still to be able to choose a different label or do you don't want them to have that ability?

29:28 Danelle Cline
Oh I think we always, they'd always need to choose, choose a different label.

29:33 Sid Mehta
Do you do Well so When you, when you are doing these bulk edits, what is the label name?

29:37 Danelle Cline
Like if you go back, Oh, I see name, I see what, yeah, yeah, that's that, that, that. Yeah, I don't, I don't know. What do you think Laura?

29:44 Praveen Palem
Yeah, I mean to make it foolproof I would say yes, let's just stick to one convention and I'll hard code it to that, that the user doesn't mess it up with it I guess.

29:53 Sid Mehta
Laura, can you go to your data set that you just showed? So like on that data, that example, what's like the label field name that you would want to, not the label itself, like not plank to the sea urchin, but what is that label called?

30:03 Praveen Palem
Mm.

30:04 Laura Chrobak
And is it the Same for every data set right now it's called Ground truth.

30:08 Sid Mehta
Okay. And that's the one that someone will go and try bulk editing and that will, is that something that's gonna remain constant for every dataset you think? Or it could be possible that we might have a, the new field called auto label and then that's the one that we want to do it on that day.

30:22 Laura Chrobak
So Right now it says ground truth. I am imagining that in our scaled workflow we change it to something like prediction. And then once that prediction is verified and all accepted then you know that leaves room for us to use ground truth when we're doing model evals with a a really reviewed set. You know, like a, okay, so right now this one says ground truth, but I think cool. Ideally we'll have prediction.

30:55 Sid Mehta
Cool. We'll just do ground truth for now and then we can teach you how to change it to like a input for this.

31:00 Danelle Cline
Okay.

31:00 Laura Chrobak
I had an idea while we were talking where in the auto labeling, the auto labeling has this ad, these labels for approval. Yeah. Would it be possible for when you change the, it's po I'm wondering if we could add the ones that we alter in the plugin for approval as well. Let's, let's do the plugin first and go through that mechanism. But maybe just marinate on that thought. It might be an interesting way to reduce how many times you're having to look at all of these, these good, good, good views.

31:49 Sid Mehta
Got it. Yeah. Makes sense.

31:51 Laura Chrobak
Yeah.

31:52 Sid Mehta
Okay. Yeah, I'll, yeah, I think, I think once we have that plugin in, you guys can use it and you can tell us, okay, here's where the gaps are now. So cool.

32:00 Laura Chrobak
Cool.

32:01 Danelle Cline
So I'm, I'm curious the, I'll, I'll just leave with this. How long did it take you to develop this plugin? How much e effort is that?

32:11 Praveen Palem
Oh, it's hardly any effort. Especially because now we have this MCP generative AI plugin into our docs.

32:22 Danelle Cline
Nice.

32:24 Praveen Palem
Actually you can actually interact with the docs and have it create the code for you. And Laura, if you're using an id, you can actually configure the MCP server in the id.

32:34 Laura Chrobak
I've done that before for, for Tater Danelle, remember?

32:37 Danelle Cline
Yeah. You haven't told me me to do that, So good.

32:42 Laura Chrobak
I I sent you the, the server link know I don't No, I don't think so.

32:46 Danelle Cline
Or if you did, I missed it.

32:48 Praveen Palem
I would love that.

32:49 Sid Mehta
Please.

32:49 Danelle Cline
So, so, but that's terrific. So it kind of lowers the, the the, the spin up to, to develop something.

32:58 Praveen Palem
Absolutely. I would, I would say take it to the grain of salt in that oh course some sometimes it can hallucinate and code's not intended. So for development purposes it's great. But as you go into UAT and production, then we would want to review line by line and make sure that somebody understands it. Because at the end of the day, you know, if, if, if your users break something, you know, you have to rely on the code.

33:24 Laura Chrobak
So How, how often do you retrain that? Like based on your updating docs?

33:31 Praveen Palem
Retrain. Retrain what?

33:33 Laura Chrobak
Well I, I imagine that it's like referencing one version of your documentation and it, it's like trained on that documentation set and then when the documentation changes you have to retrain that model.

33:49 Sid Mehta
I don't, I don't think it's like training it. I think it's like as a docs update 'cause it's using it all as context. So like, oh it's, yeah, I don't think we're like, we don't have like a custom like model. I think it's like it like it's an MCP skills like this, this is the whole like rabbit hole. I'm like, it's, it's like a new thing but now it's like I don't think you like retrain these, you you like chat GPT and call. They like use your context and of course as you update your docs it gets like better but you're basically adding it as like a skill. So this is like an MPM CT scale. I see Our doc guy is like working on like a whole like video walkthrough on it. So when it is we could send it to you. And then also, yeah, there's also like some nuances about like when you do develop plugins for 51 enterprise versus like open source, it's slightly different. 'cause like the enterprise is obviously great but like for, so right now what happens is that you're going to a certain URL and then that's where you like do all your f and enterprise. But if you, our developing plugins, we have like a slightly different workflow where we recommend where you pull up the enterprise app locally. Like you would open source. So I know you're familiar with the open source version Laura, but it's basically like you have the open source where like it will like be at a local host but then it'll still, it's the enterprise app. So it'll still work with all your cloud back media, but it's just nice to debug plugins in that mode because then it works like how you're doing an open source. So if there's any live debugging or any like print statements, it's just easier to debug. So what we generally tell people is do when you're developing plugins, do it in this like enterprise local app way. Okay then once the plugin's all good, you've tested it, then you zip it up and put it to the enterprise. Otherwise what happens is that you're like zipping, you're making changes, you're zipping it and PO posting it to 51 enterprise and then like it's not, you know, that's not the way to like debug rather you spend your time in this kind of debug mode. Once you're confident then like zipping it up and making a word in 51 enterprise is usually like, it's pretty easy. The only gotchas are like if you're using something that's like a secret, which is like an environment variable, you would need to put a secret on the deployment.

35:43 Laura Chrobak
Right.

35:44 Sid Mehta
That's like one thing. And we can show, I can, I can have Ravin send you the, just so you can guys practice and see what I'm talking about. Once you want to get into that mode, we can also send some instructions on how to get the 51 enterprise app up locally. Just so you can kind of see what that looks like and verify that works. You just, when you do that, you just might need the, your S3 credentials configured in the environment. 'cause otherwise how will it know that you can see that data?

36:07 Danelle Cline
So yes.

36:08 Sid Mehta
About it.

36:09 Danelle Cline
Terrific. Yeah.

36:10 Sid Mehta
Yeah. So we can do this all like in a walkthrough, but we can just send that information.

36:14 Danelle Cline
Yeah, that's nice that, that you have that option to do local development. Yeah, emulated.

36:20 Sid Mehta
Yeah. Yeah, yeah. It's, yeah, it like mimics open source pretty well and like yeah, open source plugin development is like, you know, pretty easy. So like we try to mimic that.

36:28 Danelle Cline
Yeah, that's really nice. Yeah.

36:30 Praveen Palem
Cool. Well, But also I want to add that that's for debugging and when something is not working, but in most cases I go by the philosophy if it, if it ain't broke, don't fix it. For the most part, generative AI is doing is getting better and better, especially cloud and 99% I've seen that it, it's, it's, it's rarely having any plugs. So for the most part it would just be developing the plugin, deploying it and while it works. But when it doesn't then we have to go down this rabbit hole. So just wanted to up there.

37:04 Laura Chrobak
Cool.

37:05 Praveen Palem
And one, one more thing that we, we discussed what the snapshot feature Lara, when you able to get, get your, get an understanding of how that works.

37:14 Laura Chrobak
Yeah.

37:15 Praveen Palem
Okay.

37:15 Laura Chrobak
Yeah.

37:17 Praveen Palem
That's amazing. Yeah, I think, I think we covered most of what we discussed last week and, and then some and, and I have notes to, to follow up with. But anything else that, oh, Danelle, were you able to shift over all of your data from open source to enterprise using that snippet I sent you?

37:39 Danelle Cline
I haven't tried.

37:41 Praveen Palem
Okay. Well we would love to stop for, love for you to stop using OSS and have it everything over and Try, try to switch over.

37:48 Danelle Cline
Okay.

37:49 Praveen Palem
Yeah, it's, it's like we'll take that.

37:52 Sid Mehta
Otherwise how, How everyone was gonna say the great work you're doing. Yeah, no, just, yeah.

37:57 Danelle Cline
Yes, yes.

37:58 Sid Mehta
So yeah. But yeah, let us know if there's any, any, any anyways you can help.

38:03 Praveen Palem
It's like going from a four to a palm to a a Mustang. We want you to have the Mustang.

38:09 Laura Chrobak
Yeah, That sounds great. I think I can, I have time this week to play around with the plugin and get back to you and we're kind of picking off bringing in our reviewers so hopefully that can manifest next week. Perfect.

38:30 Sid Mehta
Yeah.

38:31 Praveen Palem
Great.

38:31 Danelle Cline
Yes.

38:33 Laura Chrobak
And then I'm thinking that, let's just like look at a calendar really quick. So we have, I am out of office starting on February 9th and I'm actually gone through most of February. And so one thing that I'm hoping is to get that whole pipeline for Patrick to be able to change and review these labels. And then I don't think that we'll get to evaluating the model that we have on a ground truth label before then. But I think we could probably start to just at least get Danelle and I into queued up on how to do that. Okay. So we can have the ball rolling when I come back in March.

39:33 Sid Mehta
Yeah, yeah, Yeah, yeah. As long as you, yeah, we can show you whenever all you need to run model evaluations in 51 is a ground truth field and a prediction field. So any field, any data set that has both of those that you have right now, even if it's not like completely like verified and whatnot, if you have a data set like that, we would be more than happy to walk through that next time as well. It's, it's pretty easy 'cause then you just use the model evaluation panel and then that's all you need to run it. So any data set that honestly has like two fields of the same type, that's all we need. Even if it doesn't make sense, that's like fine, but we can at least show you. So then once we get to that page it's really easy. Right.

40:09 Praveen Palem
Okay. Quick question. Did we, did you al also want us to, did you also want to run the model through 51 and create the predictions or are you gonna run it externally?

40:21 Laura Chrobak
That's a good question.

40:27 Danelle Cline
I mean Probably not. I mean if it, until you guys get a GPU enabled engine, I think that our data sets are just too large.

40:38 Sid Mehta
Yeah. Yeah. So we can talk about that. I was, we do have that option now that we have for customers. So I know we're like onboarding you guys, you know, we're doing things so I don't wanna like, you know, talk about so much like, but we do have that where you can, and even on like some of the embeddings, although I do know you have your own embeddings, but like we do have the ability now for like Laura when I was showing you where you can like schedule the compute. Yeah. Right now it runs on the CPU U so there is an option to opt in on GPU as well. It will be kind of pay as you go, so you only pay for what you use. So we do have that. But yeah, I think like before that it would be good to like make sure that like we can like have like a plugin that does this for you or take your custom model. It would be able to go through a data set, add the predictions and it, you know, that would probably be the first step. And then we can probably unlock that, unlock that functionality. 'cause I assume most of the open world models that we work with in our zoo probably won't work for you.

41:31 Danelle Cline
Right, Right, right.

41:33 Laura Chrobak
Okay. So I'm, I'm hearing kind of the three separate things, right? There's this, you know, label review and updates.

41:45 Sid Mehta
Yeah.

41:45 Laura Chrobak
There's the model eval and then there's also like running the model on the data.

41:52 Sid Mehta
Yeah.

41:54 Laura Chrobak
Yeah. Let's, let's, I think for, for the end of this week and next week we can really iron out everything with that first bullet point and then come the week after probably a secret or together we can address the other two. Because I imagine they won't be as, you know, I think they'll be a little more out of the box.

42:15 Sid Mehta
Yeah, I think also like yeah, generally what we've seen from model inference, every team has their own custom one. So usually the work is like just bringing 50, just making it work with 51, you probably have your custom inference code. So it's probably just adding the labels and that's like a good first step because the main thing is first getting your labels so you can do the model eval. So that's what it is. And then we can probably then bake it out into a plugin that can then eventually use this GPU compute that we Can offer you.

42:37 Danelle Cline
Yeah, I think it would be great to have everything integrated because that just reduces the Yeah. Friction here and the, and the overhead. But I would say it's less important for our near term goals, which is to improve our model performance and our iteration on that model model.

42:55 Sid Mehta
So yeah.

42:56 Danelle Cline
Yeah, I just just wanna make sure we exercise all of the key things. 'cause I know we have a short window here to, to do that.

43:05 Sid Mehta
Yeah, yeah, definitely.

43:06 Danelle Cline
Well It's great to hear though that you guys are, you know, you, you FIT Box is working on the GPU has that now 'cause that seems pretty key for Yeah, yeah, yeah.

43:18 Sid Mehta
People have a lot of data sets and when they want embeddings or compute similarity as well.

43:23 Danelle Cline
Yeah.

43:23 Sid Mehta
They've been asking like, hey, for customers who use us for post, like, hey, I'd love if you guys gave me a GPU so I could go, you know, I could take the Mustang into a Ferrari, so, so Yeah, Well we have a fair amount of on-premise GPU capability here. Okay.

43:38 Danelle Cline
So we're not, not GPU limited. Got it. It's just our, we're integration limited.

43:45 Sid Mehta
Makes sense.

43:46 Danelle Cline
Our, our tool chains are kind of fragile.

43:49 Sid Mehta
Got it, got it.

43:49 Danelle Cline
Cool.

43:50 Sid Mehta
Yeah. Yeah, we'll take it step by step and yeah, we can, we can tack the model eval stuff after we finish this bulk edit stuff.

43:56 Praveen Palem
Yeah. And just, just so I capture this, Danelle, what's your deadline for model improvements in your project?

44:06 Danelle Cline
Well, I, we have a, a, a fall experiment and a spring experiment generally, but in this, for this particular camera, the plank devore itself, there's, I think there's actually three experiments a year and we still have yet to, we have two cameras. So we have a low and a high resolution camera. We only have one model. So the short story is we have a whole nother model to create and we have three deployments this year to apply it to. So I would say by the end, by the spring, we really need to have something working.

44:55 Praveen Palem
Okay.

44:56 Danelle Cline
And we need to have, have another model built and, and if we need to make improvements to this one, we need to have that done. So I think there, there's, there's a lot of people really interested in needing this data for their science analysis and we just currently don't have it. So we're gonna be working on not only just to context, we're gonna, we're working on proving the models, but we're also gonna be working on integrating the model output into our database, internal database so people can look at the data in the context of the vehicle, which is deployed on.

45:40 Praveen Palem
Okay, got it.

45:41 Danelle Cline
That's, there's, there's the big bigger picture it, which is super exciting. It's, there's gonna be some interesting discoveries, no doubt. So imagine, you know, we're returning in millions of, of these ROIs into a point on a plot, maybe it's bend or aggregated somehow. And then we're gonna see that in the context of all the other information where, how deep is it, what was the temperature at that point, what's the chlorophyll measurement at that point? And then we'll start making decisions based on that for our, our deployments kind thing.

46:25 Praveen Palem
Hmm.

46:26 Danelle Cline
Oh, it's, it's a bigger scheme. Yeah. We, we have a fair amount of people working on this in different facets. Some people doing the databases, you know, we're, we're kind of working on the machine learning part and there's other people working on models as well. So there are other people that will take this data that we are creating and creating different kinds of models, maybe more general, like, we're really interested in the plankton down to the lowest taxonomic level. There's some people that are interested at a higher taxonomic level, so they'll create different models. So there's lots of different players.

47:04 Praveen Palem
Got it, got it.

47:05 Danelle Cline
Yeah, that's, that's amazing.

47:06 Praveen Palem
Thanks for all that, all that information. When you say by spring, maybe when we narrow it down, do you want this done by beginning of spring? End of spring?

47:14 Danelle Cline
I don't know when the first experiment I, I'll have to get back to you on that.

47:18 Praveen Palem
Okay, sounds good.

47:20 Laura Chrobak
And does our enterprise, our initial enterprise agreement that we have paid for so far end, I believe it's end of February. Okay.

47:32 Praveen Palem
If I'm not, if I'm not wrong, Like mid-March.

47:35 Sid Mehta
Yeah, I'll have to, we'll have to look when the exact dates are. We can a Z's out this week. He's, he's in Thailand for a wedding, so he's, but yeah, we can double check with him when he comes back.

47:45 Danelle Cline
Yeah, I think by then we definitely wanna have the iteration done on this existing data set and, and any model improvements done. And that, when that's working, that sets the stage for doing another model. So I think that's where we wanna be, is just to have this model workflow completed. And when I say completed, I mean, it doesn't necessarily mean we need to be able to run our inference on the GPUs. And, and that's, that's, that's less of a concern is actually having the model working and the eval working and you know, a version one or two or three, five and then, and then we can say, go on creating the other models too. So high and low mag would be ideal, but just, just this one model is critical, I think.

48:46 Praveen Palem
Okay.

48:46 Danelle Cline
To get working. I think we're gonna work through this. I don't see any barriers in this per se at this point. It's just under us understanding the ecosystem and understanding plugins and understanding, you know, workflow and getting our users to use it and, and getting, getting that feedback done so that, you know, out of the box. It's, I, you know, there's definitely a learning curve for sure. Right. So we probably need to get our users onboarded pretty quickly here, our science users.

49:28 Praveen Palem
Got it. Yeah, that's good to know. So I will make sure that we finish the first iteration by the time the current, Yeah, I think we're moving along fine.

49:41 Sid Mehta
Okay.

49:41 Praveen Palem
Sounds good.

49:42 Danelle Cline
So yeah, that's, that's, that's great.

49:46 Praveen Palem
Okay, so next week our goal is to have the plugin installed and Yeah, and I'll send Laura the code and if Laura, if you're open to it, we could also get on a call, quick call and kind of help you set up and, and stuff like that.

50:09 Danelle Cline
And then I'm gonna try to do the community to enterprise load, make sure that works. I have an action item to load in some of our metadata too. Good. Awesome.

50:27 Sid Mehta
Right guys. Cool. All right, see you next week.

50:31 Danelle Cline
Okay. Okay.
