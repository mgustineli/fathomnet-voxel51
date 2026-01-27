## 2026-01-08 - MBARI Sync

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/50c2bf75-880a-4d67-883d-a871655b1fea

**Voxel 51 Participants:**

- Praveen Palem
- Sid Mehta

**MBARI Participants:**

- Danelle Cline
- Laura Chrobak

**Meeting Notes:**

- Demonstrated custom "edit predictions" plugin with two modes: (1) selected samples only, (2) current view excluding selections
- Discussed bulk editing workflow: filter by label → lasso/select → use plugin to change labels
- Covered tagging workflow as alternative: add tags to all → remove from exceptions → create view → bulk edit
- Introduced auto labeling panel for approving/rejecting labels (newer feature for verification workflow)
- Demonstrated compute similarity workflow: schedule background job → use sort by similarity for finding similar/duplicate samples
- Discussed verification vs label change workflows (verification as Boolean vs changing classifications)
- Planned to send updated plugin with configurable label field selection
- Action items: test plugin workflow, share Tater verification workflow video, explore auto labeling for approved labels
- Discussed snapshot feature for tracking changes and reverting to previous states

### Transcript

00:06 Praveen Palem
Hi.

00:08 Danelle Cline
Hello. How are you?

00:10 Praveen Palem
I'm good. How about yourself? Pretty good. Can you hear me okay? Okay, good. How was, how was your winter break?

00:21 Danelle Cline
Eventful. How about yours?

00:24 Praveen Palem
Yeah, same. Same. Given the state of things of the world, I would rather take non-eventful over anything else. Hey Sid.

00:38 Sid Mehta
Hello.

00:47 Praveen Palem
All right, let's give Laura and Andrew potentially a few minutes.

01:01 Danelle Cline
So Voxel is a remote first company. And do you, do you have regular meetups?

01:11 Praveen Palem
We, we actually do twice a year company retreats. We get together the entire, actually. Nice. Yeah.

01:19 Danelle Cline
That's so cool. Yeah. That's really great. And so did that, does that venue change every, Yep.

01:26 Praveen Palem
Every, every time we pick something random.

01:30 Sid Mehta
And then during the year as well, there's like a bunch of conferences. Sometimes also customer on sites as well. So then not the entire team, but then a subset of teams might, people from marketing, mainly people in customer facing roles will kind of be attendance of these. Okay, okay. Conferences, just, you know, throughout the country, like we have people, what's the one right now? CES is big. So we have some people there right now.

01:52 Danelle Cline
Yes, yes. Very good. That's, that's, that sounds like a good strategy to keep you connected and up to date.

02:01 Sid Mehta
Yeah, sure. We also do a lot of meetups as well, so if there's every, any ones that we do in the Bay Area, maybe if we're being consented that over when we do on there, I don't know where in the Bay area they do it. Maybe it's a proper, I'm not sure. But like we can at least pass on that information if you ever wanna attend. We also look for speakers as well, so if you ever wanna talk about your work at one of these, that's also on the table.

02:24 Danelle Cline
Oh, that's, that's great. Yeah, we've done that before. That can be a lot of fun. Let me just ping Laura.

02:31 Sid Mehta
Yeah.

02:32 Praveen Palem
Alright, well speaking of that, while we are waiting on the others, if you know, I mean, again, through January, if we get to a stage where, you know, you're like, Hey, we are power users of the tool. Now let's, let's take it to the next level. We could potentially come in February, do a visit and do a demo for your ML engineers across, you know, the grid team. But that's Yes there.

03:02 Danelle Cline
Yes. Thank you for that. And certainly we should keep that open. We've done that a number of times with different companies and we're, we're an interesting group. We have a very small engineering group with very diverse projects and we're very academic in that way. I suppose people are kind of isolated somehow. But this to me seems like it cuts across different projects and capabilities that we don't have. We've had a little bit of a hard time getting people on board with the idea of using external tools versus building them yourself. And I'm not a fan of building things that already exist. I mean that it's sort of, I'm stating the obvious but not always so obvious.

04:00 Laura Chrobak
Hello?

04:00 Danelle Cline
Hello. Hi Laura.

04:02 Laura Chrobak
Sorry I'm late.

04:04 Praveen Palem
You're fine.

04:05 Danelle Cline
No worries. No, we're just chitchatting.

04:11 Praveen Palem
So, so yeah. You know, just we can play it by the year and if the timing is right, whenever the timing is right, we would love to.

04:20 Danelle Cline
Yeah, we don't have to give you a tour. It's pretty cool place.

04:25 Praveen Palem
Nice.

04:27 Danelle Cline
So I don't have a whole lot to report since we last talked other than I've been using the community version to experiment a little bit and use it just actually use, try to use the tool and have, I can reflect a little bit to say I think it's kind, it's pretty intuitive to interact with the lasso tool and the grid search. It's fairly fast, which I presume has something to do with the, the database. The Mongo database is a fast query and one the sort of point where I hi hit a little bit of a roadblock was trying to do bulk edits. That felt kind of hard. Yep. So I think our users are gonna hit that pretty quickly. So that's, that's something 'cause we have this notion of validation or verification of our data.

05:31 Praveen Palem
Yeah.

05:31 Danelle Cline
And we need to flag it. So we need to find a workflow that works for that.

05:36 Praveen Palem
Yep.

05:39 Sid Mehta
And then one quick question. You said you were working on the community version, not The enterprise version We have, yeah, for my experimentation, just 'cause it's fast.

05:47 Danelle Cline
Okay. Just to run it locally.

05:49 Sid Mehta
Okay.

05:50 Danelle Cline
So if, if there's things on the, so let, let me let, let go ahead and continue with that.

05:58 Sid Mehta
Oh no, I was just asking 'cause like you guys always purchase the enterprise version. So the nice thing about the enterprise version is that the work that you do can also be seen by others. So, so, so I guess I'm curious, is there like a still reason why, like has, or do you still have like data that's like in the community version that's not on the enterprise Version?

06:14 Danelle Cline
Yeah, no, I do the, the main reason was because we don't have very many users for this account. I was just trying to be a good citizen and do it in the community and, and just understand, you know, how do you get data into it? How do we get data out of it? I think that process remains kind of the same, different, you know, keys and APIs. So, but yeah, no, I mean there's no reason it's, it's not, it's not because I don't wanna use, it's more just me trying to, we, we have accounting set up for this one project, so when we upload to the S3 buckets, it gets charged to their account. So I don't wanna have charges going across projects too, If she is using it for another project, Another project. So I'm trying to onboard other people. Yeah. Thank you for that, Laura. Im trying to onboard other people and they are excited about it. So that's not really my intention, but just, just so I can experiment a little bit with it. And I don't know if it's different, the enterprise versus the community in terms of that bulk editing flow.

07:29 Praveen Palem
Yeah, I can actually, I, I'll address that because that was one of our takeaways from, from, from last time. So I, I can actually show you because there's a plugin that I wrote and you, you know, you could, it would simplify what you're trying to do. So why don't we jump, jump right into it and then that's Terrific.

07:49 Danelle Cline
Terrific.

07:53 Laura Chrobak
Can I present my screen or do you wanna present yours?

07:55 Praveen Palem
I, I'll present because I have the plugin and then later I'll send you the code and then you can continue from there.

08:01 Laura Chrobak
Okay. Do you mind, you guys are recording this, right?

08:07 Praveen Palem
We, we, not the recording, but we, we are transcribing it.

08:12 Laura Chrobak
Would you like this to be recorded For how tos Sometimes I think it's nice just in case I forget something. Got it. Would you mind?

08:22 Praveen Palem
Yeah, no, no worries. I will do that.

08:25 Laura Chrobak
Cool. I do not have it available, so Yeah, maybe I'm gonna do that. Okay, thank you.

08:33 Praveen Palem
Alright, it's recording right now. So this is a sample data set and then we have classification labels here. And what I'm gonna do is, so I wrote this plugin called edit predictions and okay. And then what you do is, I, I didn't make it available so that you can, you can edit the entire data set because I know, you know, we want, we wanna be cautious and not give that ability, right? So for example, in this case, I'm just gonna select a few and then I'm gonna say edit predictions says three samples selected, and then I'm just randomly gonna select like knife for example, right. It execute and that's it. Three, three samples have been updated to knife and now that's it. Like, you know, this is fewer clicks than the One.

09:29 Danelle Cline
Okay. And is there, do the plugins allow this? That's great. Thank you. Do the plugins allow you to, to to, to have quick keys? Like, like control All right. To select everything.

09:49 Praveen Palem
Oh, select all the, all the samples.

09:50 Sid Mehta
You mean you, you can Like a keyboard shortcut, is that what you're asking for?

09:57 Danelle Cline
Got it.

09:58 Sid Mehta
Yeah, I like that. Yeah, we've, we've gone this especially I think we showed you our annotation features. So like people are also asking for that for annotation features. So I'll have to double check. I don't know off the top of my head. That's something we've like, but, but it, we're noticing, especially with these annotation workflows, that's where it's coming up most and we're like starting doing the rest of that. So I wanna say we can double check, but I wanna say we probably don't have shortcuts at the moment. Now whether they can be customized and plugins is also something off to, I don't know if we'll know off the top of our head. We'll have to go back.

10:26 Danelle Cline
Well imagine, you know, we have a million classifications and we wanna just look at them in the embedding view and lasso query and then validate, right? We wanna say, okay, these are good, these ones aren't and aren't. And so I'm getting a lot of noise here in background. Okay, that's better. So yeah, so that's a kind of thing that I could imagine that we would do. And that would be helpful just to do a quick lasso query control all to select everything and unselect a few things. 'cause that's often the case for the things that are, you know, that's the workflow.

11:20 Praveen Palem
Yeah, so, so like from the embeddings you can obviously like last one select them, but without using the embeddings, I don't think there's, there's this keyboard shortcut. But I will like, like said, I will double check with the team and Get back.

11:34 Danelle Cline
Yeah. One of the things I noticed was when I did that, when I lasso queried and then I tagged, let's say I put a tag on it, the tags didn't require me to select everything. Like by default the tags said, you know, e everything is gonna be tagged. So there were no extra clicks for that. But not when I had to go through the menus just to change the ground truth label. Yeah.

11:59 Sid Mehta
Yeah. So tags are kind of, yeah, that, that, that's kind of the reason for the pro. Yeah. 'cause like tagging is like, it's a bit more serious of a change when you're changing labels versus tagging. So some people will do that where they'll use tags to be like, oh, like they'll use the tags to say like, oh, change these labels. And then they'll, what you can then do is that you can create a view based on the tags. So let's say if you go through the, and we can walk through this if you have, if you wanna share your screen, but like you could do something.

12:25 Danelle Cline
Yeah. I mean if that's, if that's, that might be better sort of workflow.

12:30 Sid Mehta
Yeah, yeah.

12:31 Danelle Cline
Or what where you need to do, Yeah.

12:33 Sid Mehta
Yeah. So if you wanna go show me like one of your embeddings runs, I can kind of maybe what we can like, we can walk through that together and see that works.

12:39 Danelle Cline
Okay. I don't know, did I upload?

12:55 Sid Mehta
If not, no worries. I can also try pulling up from my End.

12:58 Danelle Cline
Yeah, I dunno if I have any, I don't have anything. Okay. Gimme one.

13:05 Laura Chrobak
For the predict, the edit predict book button that you created, could you filter like let's say as a workaround for what Danelle's trying to get at, could you filter for only a specific label and select all and then unselect the ones you don't want? It's just, that's usually more likely of a case. Usually we have to, we're like making changes to the majority of the class rather than the minority.

13:35 Praveen Palem
Got it. Got it. So let's think through this. So you would have a dropdown and say select you select a label and then, okay, so we could do it both ways, right? One is you pre-select some images, if that's the case.

13:49 Laura Chrobak
Yeah.

13:50 Praveen Palem
Then you would not have the dropdown. But if you don't select any images, then you would have the dropdown that would say, okay, apply this to all of these classes.

13:59 Laura Chrobak
Hmm.

14:00 Praveen Palem
How does that sound?

14:04 Laura Chrobak
I think that, You know, I think we want both workflows. So we want the workflow to be able to either select it from the vector space and then unselect a few or select a subset of that and change.

14:18 Praveen Palem
Yeah. So this what, what I'm explaining to you covers both cases, right? If there's selections then it would, it would work as if whatever I showed you right now. Right, Right.

14:28 Laura Chrobak
You just showed us. Yeah.

14:29 Praveen Palem
Yeah. If there's no selections, then you would have a dropdown to start with to say okay, I'm gonna select this class and then for all of the images of that class, I'm gonna select a new class. So you have two dropdowns, Right?

14:45 Laura Chrobak
Is that not already? Is that first step not already a feature just to filter on class?

14:52 Praveen Palem
Oh yeah, actually you could. You could do that by just using the labels.

14:58 Sid Mehta
Yeah. The sidebar. You could also use the sidebar. Yeah. For That.

15:01 Praveen Palem
Yeah.

15:02 Laura Chrobak
Okay. And then you can select everything there.

15:05 Praveen Palem
Yep.

15:06 Laura Chrobak
Except, is there a way to do that without having to physically select everything? Could you, you filter and then say select all and then use your edit, well your edit to say change everything that I've selected.

15:20 Praveen Palem
Yeah, that's exactly how it works. So yeah.

15:22 Laura Chrobak
So can You show me the select all like work through?

15:27 Praveen Palem
Sure.

15:29 Danelle Cline
Danelle did, did you wanna share your screen or do you want me to, Oh, I don't have my, my my local things up, but I guess we could go into our enterprise version. Yeah.

15:43 Laura Chrobak
Do you want me to showcase that?

15:45 Danelle Cline
If you have that? I don't have that one handy. I think I computed the embeddings for that. So it should work.

15:55 Sid Mehta
Yeah. So if you go to plus button and then we see embeddings, we can see if there's any embeddings on this data set then. And then hit plus again. Oh, it looks like there's not, or select brain key. If you go to select brain key, sorry, select frame key next to it. If there's anything that comes up. Yeah, there we go. Okay. Yeah, so if we now go to the split view. So if you go to the plus button, there's like the two side by side rectangles. Yeah. And if you wanna color by anything to make it more helpful and useful label maybe.

16:46 Danelle Cline
And it's fine to make changes in here. I I, I haven't loaded up our latest data set, so, okay, Cool.

16:56 Sid Mehta
Okay, so now you want to, so yeah, I guess like could you give like a lasso example of what you would want to, Okay, so I've selected, maybe I'm gonna redo that.

17:05 Laura Chrobak
It was a little wonky. Go ahead, Select One More time. Hold On. Okay, here, Here we go. Okay, this is the What we want.

17:23 Sid Mehta
Okay, so all these samples and then now what you would want to do in this scenario, like Let's say this is all wrong.

17:31 Laura Chrobak
Can I select all and make the change?

17:36 Sid Mehta
Yeah.

17:36 Laura Chrobak
Except for this one.

17:40 Sid Mehta
Yeah, that's, I do. I feel like that should be a thing. I feel like I've definitely seen the select all. I feel like I've seen that. That's a good question. So normally what people will do, another thing is like if you create like a view and then you can work on the view as well. So you could save this as like a, if you go to now the unsaved, you could also save this as a view. So if you go to unsaved view on the top left, and then you can save now see what happens if you do save current filters as view. So then you could save this as like, yeah, test view. So okay, now if we do that, so now it's like saved as a view and now you're seeing all, and so now this view will, you can always go back and see like these samples. Yeah, I'm like curious Pravin, the plugin that you did, would it be able to work on a view?

18:46 Praveen Palem
Yeah. Like Not, not at the moment, but you know it's, it's all code. So you could change it to select current view or selections so we could change it With this view.

18:56 Sid Mehta
Yeah. So that can be another thing. You can make it select like a view or target. If clicking is like too much, you can create views of, of stuff. And then that way you have this view and then you can just say on this view and then you can maybe then delete this view if you, if you don't need it afterwards. 'cause it's like the fixed view. Another thing that, yeah, sorry, go Ahead.

19:15 Praveen Palem
The only case that it wouldn't cover is if she wanted to do all of the, all of these hundred or whatever, but except for one, that's one thing that Laura mentioned.

19:26 Sid Mehta
Got it.

19:27 Praveen Palem
Got it.

19:28 Sid Mehta
Okay. Let me see how you do select all. Why do I feel like I've seen that before?

19:38 Praveen Palem
So, so yeah, I, I think, I think we might come up with a way to do that, but, but that's something that you, you are thinking would be a potential workflow, right? You select some samples but then you also unselect some of those.

19:53 Laura Chrobak
Yeah, so I can kind of, if it helps in our old workflow, what we would have is we have all of these classifications and our experts would buy, they would, they would buy class, do the review. So they start with class one and they filter for that for everything in that class. And in this case we were actually, we had pre clustered them, so we filtered everything in one cluster and that cluster had a mix of different classes. But usually it's the majority one and then they clean that bulk. And sometimes that's a matter of clicking a small subset, changing those and moving on. Sometimes that's a matter of saying everything here has been this classified select all of it and change.

20:45 Sid Mehta
Okay. So I'm wondering if we can try tagging then. So like if you see where tag is, 'cause then if you go to where, so if you see where the paint, I forget what that's even called, but it's like, yeah, so you can like tag all these ones as like to do or like whatever tag you want or like review or change. And then if there was one that didn't needed to be, you could remove the tag from that one and then that might be an easier way to manage it.

21:10 Laura Chrobak
I'm Thinking, can you show me how to make the tag selection for just a subset?

21:18 Sid Mehta
So just a subset here or like, Or sorry.

21:22 Laura Chrobak
So I just created that tag, right?

21:25 Sid Mehta
Did you actually create it?

21:26 Laura Chrobak
Because I thought I did.

21:27 Sid Mehta
Okay.

21:28 Laura Chrobak
Okay. To do and then, yeah. Oh, do I need to click on something?

21:34 Sid Mehta
Well, I think there was the add to do tags to 243 samples underneath. So if you, yeah, if you just type it again. So if you do to do and then yeah, click, click Enter.

21:46 Laura Chrobak
Yeah, that's what you have to, There you go.

21:48 Sid Mehta
Okay. And Then apply.

21:49 Laura Chrobak
I'm gonna have to apply. Yeah. Okay. What if I wanted, don't you do the subset.

21:56 Sid Mehta
So subset, so how, how would you come across a subset?

21:58 Laura Chrobak
Like just manually or like in the lasso or how would you come across a subset Or let's say I want to change 95% of these, so, but I don't wanna click through each one. And by change, I mean add the tag two.

22:16 Sid Mehta
You would, so, okay, so you want to, I'm, I'm a little confused. So you have 243 samples here. How, how are you selecting which ones you don't want to change?

22:26 Laura Chrobak
Which ones I don't want to add the tag to.

22:29 Sid Mehta
Is that Or, or which ones you wanna remove the tag to, right, because all of them have the tag.

22:32 Laura Chrobak
So which ones did you wanna remove the tag to?

22:34 Sid Mehta
How would you decide that?

22:37 Laura Chrobak
So let's say this is, let's say this isn't a great example, but let's say this particular one is not a nano plankton, it's something else.

22:50 Sid Mehta
Okay. Yeah. Yeah. So if you were to go, then you can just remove the tag on that one and then that's how you would like, and then you can, you can go through and probably select, and I think you can do something where you can deselect all the ones and then remove the tags from the deselected ones.

23:04 Laura Chrobak
Okay. So if I wanted to, first I make a tag on the whole set and then I want to remove the tag from these, how do I do that?

23:14 Sid Mehta
So now I think if you go to tag and then to do and then apply. So I think the tags should be removed.

23:28 Danelle Cline
Yeah. We just don't have the, you don't have the, the, the tags aren't visible On the, yeah, It's interesting because the sample count seems to remain the same.

23:39 Sid Mehta
Yeah, because the sample, because the sample count is based on the view, right? So those are still in the view. So now what we can do, so if, if we exit out this field, let's go complete, right? Let, let's just exit out. So if you, yeah, so now we have all of our data set. Now if you go to the sample tags on the left and could have the to-do so, yeah, it's not too four, I think we removed someone, right? So the ones that were removed are now 2 38. Does that make sense? Because we've removed some of those tags. So I think we removed five, right? So that's how it is. So yeah, no, but, but yeah. So I guess like in your scenario, right, you would, it's like the way this was designed was to be more like the opposite, right? Where it's like you might have like in a needle of a haystack, you have like maybe five or 10 that you want to do where it's like you guys are kind of doing the opposite. It's like, oh we actually wanna do the bulk. But then there's like, but then 90 or 90% of them will want, but then the 10% will need to change. So for that you might, it might be easier to like give them all like the to do tag and then just remove the ones that you want rather than going the opposite, right? Because otherwise you're gonna spend way more time adding 238 tags. So rather than adding 238 tags, it's probably just easier to remove five. Right.

24:57 Praveen Palem
Right.

24:58 Laura Chrobak
Okay. So now that I have these tagged and maybe I type in their alternative name somehow or Yeah.

25:09 Sid Mehta
So then I think, oh, now, now, now you wanna actually do the label switch.

25:13 Laura Chrobak
Yeah.

25:14 Sid Mehta
Yeah. This is the, when it probably makes sense to use pra being's plugin where like if, if Pravin, I don't know if it's possible, if you can like make the plugin work on a view, what I would do then is like now after you've gone through and tagged, that's probably when I would create a view, which is this to-do view. And then I would use Pravin then plugin to then change it on those ones. So it changes only on the ones that adhere to this.

25:36 Laura Chrobak
I see out curiosity. How do other clients typically go about bulk name changes? Is that, is that just not something other challenges are needing?

25:51 Sid Mehta
It it, it does come a little less because I'll be honest, most of them will like find annotation mistakes in their tool. But like it won't be like bulk, right? It might be like one or two. So, but, but that, but it is something we were hoping to like look out more. 'cause that is one of the advantages of the tool and whatnot and how to do that. But yeah, I'll be honest, it's like most of the annotation mistakes that we have been have been more kind of on a, like a smaller scale. But no, this is very interesting and I think it's like a good, some good feedback. We'll we can take about like supporting more bulk annotation stuff.

26:24 Laura Chrobak
So yeah, just because I want to iterate on, I don't wanna necessarily zone in on one one solution just quite yet. 'cause I think that there might be some other options. And this tagging mechanism is a little bit more complicated than I was hoping for. Is it, what if, so we have a lot of annotations and we don't actually need all of them. Would it be simpler to just delete them or something like that?

26:57 Sid Mehta
Delete annotations. Like in what sense?

27:00 Laura Chrobak
Like let's say, I think you obviously mean, sorry, go ahead. We need this bulk change element for, for some moves, but in other senses it might be simpler for us just to say like, rather than having to change the name for these four, just get rid of them.

27:27 Sid Mehta
Oh, just deleting them.

27:29 Laura Chrobak
Yeah.

27:31 Sid Mehta
Yeah. I mean that's also, you know, fair. I'm just trying to think if it actually like, 'cause it's the same thing, right? It's like you delete them and then, yeah, I think we have like a delete selected samples field. So you, it would just be the operator and then you can run on the selected ones and then that should delete them. So that can also work as well if you would just wanna delete the ones that are badly annotated.

27:52 Danelle Cline
Let's, let's Do that. Let's do that just to go through that exercise. Yes. How do you do that?

27:57 Sid Mehta
So I believe it's a built-in one. It should be called delete se selected samples. So if you go to the hamburger menu, so near the five check mark. So down, yeah, down where the buttons are. So there's like the five with the check mark next to it, right? 'cause of the five that you've selected and then there's the hamburger menu. Oh, okay. So now it's near the settings. So sorry, go to the gear. Go to the Gear and then left of that. So that's the hamburger menu. We call it the browse operation. So if you do delete selected samp selected samples, you have to select samples to delete. But the five that, for example JGFG would just delete those samples and then yeah, it would delete it from this dataset.

28:43 Praveen Palem
Okay. You just delete labels also is available. So if you wanna keep the sample but delete the labels, that's also available.

28:49 Sid Mehta
Yeah, That's also true. Yeah.

28:51 Danelle Cline
Is there a way to button it? Is there a way to pin that to your menu so you don't have to keep going? Amber?

28:58 Sid Mehta
Yeah, Does, Yeah.

28:59 Praveen Palem
Actually if you hit the Eric to showed it last week, but if you hit the Tilda button, it'll, it's a strategic market and then the most recently used ones will stay on the top.

29:09 Sid Mehta
Okay. But I guess you're asking, do you, if you can make it like a button, so the, the ones down there are like considered buttons, so were there a bit more accessible, right? Like the settings and whatnot. So is that what you're asking Danielle? So if you can make it into a button.

29:23 Laura Chrobak
Yeah, like the plugin one was when you showed us it was just in this bar. Right?

29:30 Sid Mehta
Okay. Yeah. Yeah. So that's like a thing, a setting. So yeah, it's a built-in plugin. But yeah, I think Ravin, that shouldn't be too much. Like if you were to take basically the, this plugin that's already written and then just make it, send them a version that they can use as like a button that's also that, that's something we could do. Yeah.

29:47 Laura Chrobak
Okay. So we can't pin these to a bar, we just go through and find them.

29:51 Sid Mehta
No, I, I think we should be able to, I think upper, maybe you can take that as an ar. He can like, 'cause these, these are built-in plugins, right? But we can give you a version of this that's like, and Barry's very special button plugin and then, we'll that's what it'll be called and it'll just be, and then it would be the exact same thing, but it'll just be more visible. Okay. Unless there's a way that we have a way to make built-in plugins more visible. But yeah, there should be a workaround. Long story short.

30:17 Praveen Palem
Okay.

30:18 Danelle Cline
So I can see that being helpful for that. And other things too, like if there's, you know, a lot of times we have like this unknown or junk or some other category where we just wanna put it in there and it, you know, having a, a plugin that does that.

30:37 Praveen Palem
Yeah, Yeah. I can send you the, those plugins. Can you tell me, confirm which ones you need? Do you need the delete samples or delete labels or both?

30:46 Laura Chrobak
I think that we need to orient around our workflow and I can email you that once I know, but for now, the, actually could you explain to me what this delete selected labels one does?

31:02 Sid Mehta
Yeah, so the first one was like delete samples, right? So if you had 7,000 samples right, you would have five less. Now this one, what it's doing is just, it's deleting the label. So it's not deleting the samples. So you have 7,000 samples, but if you had now 7,000 labels, now you have less labels. So it would just be you, it would just be a sample without a label Now.

31:23 Laura Chrobak
Okay. There's an image without a label in there.

31:25 Sid Mehta
Yes, exactly.

31:27 Laura Chrobak
Okay. Can I filter for images without labels?

31:35 Sid Mehta
Oh that's, that's a good one. It doesn't come. There's probably something, there's probably some way to do that. Yes. I'll have to think if it's in the UI or in the sdk, but like, yeah, I, I don't think it comes up as like none Because it, here you can filter for the one you have the room labels, but without right now.

31:55 Danelle Cline
Hey Guys, I have to jump, I have a conference room and I, I've, I got booted.

32:02 Sid Mehta
Okay, no worries.

32:03 Danelle Cline
But, but send us the, send us the plugins and I'll, I'll look at integrating that.

32:09 Praveen Palem
Okay, sounds good. Got It.

32:11 Sid Mehta
Yeah.

32:11 Danelle Cline
Okay. Thank you. Bye.

32:13 Sid Mehta
Yeah, Yeah, that's, yeah. I'll have to see Laura if, if, if there's a good way to do that. 'cause I assume you would want it in the app. I know in the SDK it's like completely possible. Like there's like a, it's basically doing a check on if this field exists. But then I'm just trying to think whether in the app we make it kind of easy to do that.

32:32 Laura Chrobak
I don't think it would be a P zero thing, but it's always a nice Yeah, little interesting yeah.

32:39 Sid Mehta
Element. Yeah. Yeah we can definitely do it in the sdk 'cause that's like, that's actually like a common search people do. But then I'll have to see how it manifests in the app. 'cause if it doesn't exist then I don't, I'm not sure if it's like a, 'cause if we're de deleting the label then it's like the label doesn't exist so it's, I don't think it'll even show up as none. But I'll have to double check. Double check.

32:58 Laura Chrobak
Okay.

32:59 Praveen Palem
Yeah, yeah.

32:59 Laura Chrobak
Right now.

33:00 Praveen Palem
So we'll check with the product on that. But Laura, I ask you, you mentioned the workflow, right? I think if you could share your entire workflow we could probably brainstorm and come up with a, with with a good set of changes or plugins needed to accomplish it, right?

33:18 Laura Chrobak
Yeah, yeah, Yeah.

33:20 Sid Mehta
It's already helpful. You tell us, telling us that like mostly I want, we'll want to bulk, bulk edit but I might not. Right? So that's why I think the tagging thing, at least I know it's not the most easiest thing, but it makes more sense in your use useful because it's easier to just like, you know, say change this, but then just untag the ones that you don't wanna change.

33:37 Laura Chrobak
Yeah. So let's see if I can easily get to, so this is Tater and it is a product created by Sea Vision, which is the small started in Boston.

34:06 Sid Mehta
Hmm.

34:06 Laura Chrobak
And what we typically do is we have hmm our data set, these are just different folders and you can filter on different elements. And so for instance, I might filter for a specific label that equals, usually I filter on cluster. Let's do that first. Cluster includes C one maybe. Let's see if that does anything. Okay. Now we wait for some unknown period of time. Okay. Did that change the number of files?

34:57 Praveen Palem
Yeah.

34:58 Laura Chrobak
Yeah. Okay, great. Okay, so now we see, oh interesting. Hold on. I think this is the view that I want. So this is not the view that I'm looking for. Hold on. Yeah, that one right there in a little bit better. That's all right. We're gonna get, yeah. Is this So something that, sorry, I'm running into this issue where usually it allows me to select all of these and it's not right now. I would normally ask Janelle why this is not looking like it used to. It's possible she altered the dataset since last time I used it. But Talking by the 51 or the other tool In other tool. Okay. But I think that sounds, I would love, I would love to visually show it to you, but what I just described is the bulk of it maybe. And maybe I can make a little video recording and send it to you all once I I get that.

37:30 Sid Mehta
Yeah.

37:31 Praveen Palem
Squared away. Okay.

37:36 Laura Chrobak
One element that we didn't broach that I'm wondering if it would be useful to incorporate into this plugin is that Oh right, right, right. So in our previous workflow, as I described, a person is looking at the cluster and they see all these different classifications. Some of them are wrong. The ones that are correct, they verify the ones that are not correct, they don't verify. And in tater those are the two options that you have. You can verify things or you cannot verify things. So that's why we want this ability to switch names over. But we have essentially a, a manual way to indicate the changes that we need and that we have an Excel spreadsheet and if the, if the cluster is should be pri primarily another name but currently has a different class that's noted in the Excel spreadsheet and then we make that bulk change on the backend. So we said, we say everything that's been verified is correct gets this bulk name change.

38:54 Sid Mehta
So like I guess that's like another, and then how would you bring in those verifications into 51?

39:02 Laura Chrobak
You were thinking Well the verification isn't necess in this, in this case it's just acting like a tag, right? It's just telling us which ones we wanna keep. Yeah. And so in this case, I don't think we need the, we don't need the verification element. We just need to be able to say this subset we either want to make a change to or we want to keep and not make it make a change to, because let's say they were all, let's say the majority of them are right and some sub minority is incorrect and we just let those be and we remove them from the data set. Yeah. The phone's not turning back on so, Got it.

39:46 Sid Mehta
Alright. Yeah. I'm also wondering, so we do have this like auto labeling feature now where you can bring your own labels into 51 and then use them to like approve some labels and reject some labels. So I'm wondering if that might also work for you as well. It's kind of a similar workflow to what you're talking about, but like essentially what happens is that you have, and I think it's on your deployment right now. So if we go to the samples plus Auto Labeling Request, Like and then go to analyze existing labels and then select your label field so through, and then just give it like a, you can call it GT or something.

40:30 Laura Chrobak
Oh That's supposed to, perfect. Thank you.

40:33 Sid Mehta
Just and then analyze labels. I would schedule it on teams.

40:35 Laura Chrobak
Do Okay.

40:39 Sid Mehta
Yeah, this will, this might take a little bit, but yeah, we can try. I'm wondering if this might be useful because it's like basically this idea of like let's assume these labels came from an auto label or if they even came from a ground truth annotation. If you want to approve and reject labels and then just like keep tabs on that. I'm just wondering if it's easy. And then you can also filter by class as well. So you can filter by like all the different classes that you have and then you can choose to approve these labels, promote these labels. So I'm wondering if this workflow might be more geared towards you than the kind of tag one. This is a relatively new feature, so, but I'm wondering if this, we can try this out. This might take a, if you go to the runs page, I'm wondering if we can see the progress.

41:24 Praveen Palem
Okay.

41:24 Sid Mehta
It should, so if you go to samples, so if we go to the auto labeling now if you go back, yeah, if you, sorry, hit the back button. You analyze existing labels. Good.

41:37 Laura Chrobak
Yeah.

41:38 Sid Mehta
So if you click there, Is it, So yeah, I guess the confidence and then if you could close the embeddings panel and then go back to the side by side. So the auto labeling panel and the samples greater are side by side. So here I'm wondering if this is interesting for you. So this is like another way of kind of viewing the same thing. But you see all your data here and then you can kick on a class and it'll show you all the samples in that class. So it'll show you this ones. Now if you go down here, you have like add these a hundred labels for approval and then it'll approve. But then I believe we also have the ability to then I think I'll have to, I'll have to play around with this, but I'm wondering if like it's, it's more or less the same thing. You can choose to like, hey I wanna approve these labels. And then you can also then delete labels or delete samples where maybe you don't want to improve and only keep those once Can I have different confidences for different, Yeah, so you can filter out the confidences as well. So if you only wanna do high level confidence, that's also coming. Do you have confidence values on these?

42:51 Laura Chrobak
Yeah.

42:53 Sid Mehta
Oh these come with confidence values.

42:55 Laura Chrobak
They should.

42:57 Sid Mehta
Oh okay. It doesn't seem like, 'cause they're all, they all seem to be one for all of them.

43:01 Laura Chrobak
Yeah, well that seems like a mistake.

43:05 Sid Mehta
Yeah, I'll look into the data set on when we One, but yeah, I, we can send you the docs for this as well and you can kind of read through those about the label. This is also a relatively new feature, but it's about like basically approving and rejecting labels, which sounds like a little bit like your workflow.

43:23 Laura Chrobak
So What happens if I add labels for approval If you add labels?

43:28 Sid Mehta
So it would yeah, add those labels then to the field and then anything that you actually, you know what, let me, let me read about this one. I mi I, I might, yeah, let me, let me let yeah get back to you on this one because it's a relatively new feature. 'cause yeah, there's like there used to and it's also changed. There used to be like you add them to approval and then you do a final approval. But now I think it's like one approval but basically these ones were being like, these are labels that have accepted and then whatever doesn't get accepted essentially gets deleted.

43:59 Laura Chrobak
Okay. I think that this could be really valuable for, 'cause I think we kind of identified these two cases where in one case basically the entire cluster is incorrectly labeled or in another case the majority of them are, but not all of them are. Correct. And so it sounds like the plugin can address that former case and that this could potentially address the, the other where most of the labels are Correct. And you just wanna give them a thumbs up.

44:35 Sid Mehta
Yeah, yeah, that's essentially it. That's basically what you're doing approval or whatnot. And then if you don't want those then you can delete those labels or as well and they, they just won't be there anymore.

44:46 Laura Chrobak
Yeah, I do wanna see what the approval workflow is mixed. Yeah. Just because if it means having, like for instance if my, if Patrick can look at all of these AKAs here and say this is clearly this class 'cause they all look like this little Yeah cute guy. Then I don't want him to have to go through each individual one. Right. Like he can easily see from here that it's all Okay.

45:19 Sid Mehta
Yeah, I can send you the docs on these that we can read. I'll also try it out myself. But yeah, we basically, it's basically in this section of our docs. Like I said it's a relatively new feature. So like there, I'll put it here but then Pravin, you can also put this as like a follow up. So it might also just be like an interesting Yeah. Thing that can go Additional tool. Yeah, Additional tool.

45:45 Laura Chrobak
Yeah.

45:46 Sid Mehta
Promoting. Yeah. So as you, yeah, if we, if I go here, so as you promote you can promote labels of approval by clicking a at the bottom. This one just there. I think you can go class by class but yeah, let me play around with the tool and Pravin I can play around tone and I are into kings and scene, but if it might be good for this use case.

46:11 Praveen Palem
Okay, so, So, so just just so I'm clear, the plugin, it would be useful when you have only a few that are wrong, right? I'm trying Tom, trying to understand in which case the plugin would be useful versus this one.

46:33 Laura Chrobak
It's still unclear to me in which case this is useful 'cause I don't really know what this next step looks like. So maybe question mark over this the maybe I think that it would be helpful to understand what this mechanism is and then we can decide how we wanna change the book plugin.

46:56 Sid Mehta
Right.

46:58 Praveen Palem
Okay. Yeah. Yeah. I kind of feel like we could condense them down into one or the other but you know, just to keep it simple, but again, I would, I wouldn't wanna make a, make a decision unless, until I all of us understand this auto label feature and then maybe I could send you a brief on Slack or you know, something and we can definitely touch base next week and discuss. Okay.

47:24 Laura Chrobak
The other two elements I wanted to talk about is, is there any facility for QAQC for assigning any review or anything like that? Like assigning review of specific parts of the dataset to specific people?

47:57 Sid Mehta
Not at the moment. We mainly, it's mainly more just you tag, like I've seen people just tag and then sometimes they'll just put the person's name like you know, Laura's to review and then they'll put that as like a tag. So that's like one thing that I've seen maybe just within tagging, but there's no way to like at mention like, hey review this.

48:15 Laura Chrobak
Okay. Yeah.

48:16 Sid Mehta
Yeah. These are kind of, yeah, things that we're thinking about bringing to the platform as we expand annotation capabilities.

48:21 Laura Chrobak
But, And then how about, I think this might fall under the realm of plugins, but one thing that I, or just in context to either how this auto labeling feature works or the bulk plugin. One thing that I want to avoid is type errors when we do make these label changes. So it would be helpful if we do end up building the, the bulk plugin to have the change be constrained to the existing ground truth labels within the dataset.

49:12 Sid Mehta
What do you mean by like what's the type error that you're foreseeing that you wanna avoid?

49:15 Laura Chrobak
Yeah, so for, for example, let's say I wanted like I was able to change this with a plugin to say like all of these get a new class, right?

49:27 Sid Mehta
And so I type in a New class, meaning a new label, like an new entirely new label.

49:31 Laura Chrobak
Okay, a new label and I type in nano plankton but I spell it wrong. Now that is hard when I'm reviewing my dataset because I like, I as the person who's reviewing all the data don't know that there's a spelling error. And so I have to be like, oh look this wasn't found when I'm like doing my data review. And so sometimes you can, if you're doing like a name change, you can say it's constrained to only this set of classes, this label use this set of labels.

50:10 Praveen Palem
Got it.

50:11 Sid Mehta
Yeah. Yeah. That's something probably that can be changed in the plugin is that you can probably give it like a dropdown menu only rather than them typing it out. So that can be, that can be, that's again, yeah, like one thing that we'll do is that like we'll kind of send you maybe what once we line upon like a good, our sparring point, we'll probably send you the plugin but then you can also modify that plugin to be like great, however it is for your case. Right? So that's the idea with plugins is that we, you know, there's generally ones that you can take as like a starting point, but then it's only really someone who knows your workflows where your data set we can kind of modify and change those to work for viewers.

50:47 Laura Chrobak
Okay.

50:47 Sid Mehta
Yeah. Yeah. But yeah that that like with vin's plugin where like if you want to, that can totally be changed where like the second option of what to change it to can just come from a dropdown menu.

50:57 Laura Chrobak
Awesome.

50:59 Sid Mehta
Cool. Any other questions?

51:09 Laura Chrobak
I don't think that we've gone over similarity search. Could we just walk through that together?

51:16 Sid Mehta
Yeah, so I think you have the brain functionality here. So what you, if you can, if you can click X at the very, so you can click at the, in the view bar, if you could click X there. Yeah, I'd just like to work there. And if you go back to the hamburger menu, so then what you'll need to first do is that you'll need to compute similarity first and then you'll need to like run this form to compute similarity. And then so you, you give it some brain Cree, you choose an embeddings model? I don't a sample field containing, yeah, I think you can just choose the model here. Oh yeah, you need to type the brain key in. So I would just, but yeah, it, it only has like a certain type so I would just call it test sim for now.

52:13 Laura Chrobak
Yeah.

52:14 Sid Mehta
And yeah, it, it can't have spaces or underscores. It's, yeah, it, it'll yell at you till you do that and optional. I don't think the sample field is what is. Oh okay. I guess you could use those or if you want to compute them again.

52:31 Praveen Palem
Yeah, but I think maybe you should just put it in new field name.

52:34 Sid Mehta
It'll store the, yeah so, but yeah this will basically compute the similarity and then eventually and create the indexes and then you'll have to call sort by similarity to actually do this. So let me just confirm on this. So if we do start just my end. So yeah, so if we call this test sim Yeah. So we can run execute on this and then I would just schedule it as a do, sorry, I would schedule, oh sorry, wasn't supposed to do that. You're supposed to schedule it on do so I think it do it right? No it doesn't. Yeah. Is it, is the app gonna hang? Okay, maybe it didn't run let's go to runs. No, 'cause if it didn't, yeah it wouldn't have 'cause she hit execute. Right? So if it needs to be scheduled, so yeah, let's redo that. I'm not sure if it ran and we'll have to give it a new similarity name. So let's call this test sim two. And then, so are these embeddings that you have on there, these ground truth do log logs?

53:53 Laura Chrobak
I'm not sure then I'll look at them. Okay.

53:56 Sid Mehta
Yeah, so I would just not then let's maybe exit that out and just, no, no, sorry. Okay, let's try this again. Let's go to compute similarity. So, okay. And then do not go to the embeddings thing, please go to the model and then just choose like one of the models here. I would maybe do, yeah, we can do clip. That's fine. And then all these other stuff is like fine sk learn all this stuff and then oh, oh, and then instead of execute there's a dropdown carrot menu to execute. And then, and then if you do schedule on do is what you need to select The number workers is negative 10.

54:38 Laura Chrobak
Hmm.

54:40 Praveen Palem
Yeah, yeah.

54:41 Sid Mehta
I'm gonna also just, let's just for the time, let's just, I make it zero for or like yeah or four. Yeah, I, I wouldn't complicate it right now I just wanna make sure that this runs. So, and then please and then drop down care and then schedule so it runs in the background Unfortunately. Oh Yeah, it's, yeah, that's like a known bug. Okay, now we should see it running. Okay. And then it'll run and then what will happen next is that then you'll want to sort by similarity. So if you go to samples back, you'll type in the sort by similarity plugin and then you'll eventually, 'cause what that compute by similarity do is it's, it's doing the index for similarity and then you'll eventually sort by that similarity. So if you go and type sort by similarity and then yeah, eventually what's gonna happen. So it's you're, there's no, when the run finishes you should be able to see the brain key there that you can select for. And then I can share my screen of what it'll look like. So if we go here, so this is what it looks like on my end, like I should be able to see this brain key that I ran before. So you should be able to see test them too. And then I can choose to do it by like I select some images and I'm trying to find similar ones like that. Or I can input an image locally and do it there. Text is only available for certain ones. So like you did cliff embedding, so you might be able to do text as well and you can test that. But yeah, that's basically more or less how it works and then you can specify the number of max matches you want for that.

56:22 Laura Chrobak
Cool.

56:23 Praveen Palem
Okay.

56:23 Laura Chrobak
I'll play around with that. So just to recap, since we only have a couple more minutes, I can send you guys a quick tater example of the verification process that we currently have. Yep. You all can send me the auto labeling information and then with that I think we can kind of maybe on Slack brainstorm and agree upon what path we want to move forward, if that includes a plugin or not. I will test out this similarity search. I think Danelle and I are, are going to re-upload the dataset and next week I would also love to kind of go through any provisions that you guys suggest that we do to make sure we don't mess anything, anyone can mess anything up too much or like how to recover from big changes. I feel like that would be helpful for me to know, like maybe going back in history and reverting or Yeah, actually we, I think we recorded last week's last time where Eric specifically showed the snapshot feature.

57:39 Praveen Palem
Okay. But yeah, if, if, if the recording's available I will point you to it but, but either way I will also send you links to how, how to use the snapshot feature.

57:50 Laura Chrobak
Cool. Yeah and if there are any other, you know, feature capabilities that we haven't mentioned that you think would be useful for what you think this project is like, please let me know. I'm not married to anything that we're currently doing here.

58:11 Sid Mehta
So Yeah, I think the main thing, it's good that you guys are looking at embeddings, the brain functionality, obviously editing and editing labels. The other big value is model evaluation. So we can talk about that. But basically for that, all you'll need is to a way to get your model predictions back into 51. And once you have that, it's pretty easy then to run like an evaluation run, find those false positives, false negatives. So, but yeah, you know, we have some time we don't need to, we don't need to conquer Rome in a day so, you know, so we can, but yeah, that's definitely one thing that we haven't really explored. We're kind of talking about a lot of stuff that's like for pre-training but then post-training we have a lot of cool model evaluation features which we, we could talk to and yeah, it's, it's pretty easy to run And yeah and the, I guess the overarching, one of the other features is the dashboard where you can create custom plots.

59:00 Praveen Palem
We did mention, mention that in the, in slack, but you know, that's also something, I don't know if, if that's useful, but you could create all sorts of like scattered plots, pipe plots, that sort of stuff using their data.

59:13 Laura Chrobak
Right. Yeah I remember seeing some of that. The, yeah that's gonna be so useful. We have one data set that isn't this, that has like perfectly covered each reviewed ground truth that maybe after I feel more comfortable with the label review workflow, we can transition into talking about model eval on that data set. Cool. That's good. Alright, well thank you guys so much. I really appreciate it.

59:46 Praveen Palem
Yeah, anytime. Yeah, if you, any questions feel free to use Slack as always and I will talk to you again next Thursday. Cool.

59:58 Laura Chrobak
Yeah, sounds good.

1:00:00 Praveen Palem
Okay, thank you.
