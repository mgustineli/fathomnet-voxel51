## 2025-12-15 MBARI Success Criteria Meeting

**Meeting Recording:** https://app.attention.tech/conversations/all-calls/d61c0da0-5a56-4cd2-941a-89b41248be3d

**Voxel 51 Participants:**

- Sid Mehta
- Praveen Palem

**MBARI Participants:**

- Danelle Cline
- Andrew McCann

**Meeting Notes:**

- Resolved SSO and AWS credential configuration (discussed rotation strategies and long-lived tokens with scoped permissions)
- Walked through dataset ingestion workflow: configuring cloud credentials → setting API keys → loading S3 data → computing metadata
- Covered delegated operators for background processing (embeddings, CPU backend with potential GPU access coming)
- Introduced model evaluation features: precision/recall metrics, confusion matrices, scenario analysis
- Discussed Dino model with 8-pixel block size for small grainy plankton data
- Enabled alpha annotation features with constrained label schemas to prevent typos
- Reviewed plugins ecosystem: brain (similarity/uniqueness), dashboard (custom plots), io, utils
- Addressed external collaborator access challenges (SSO limitations for non-MBARI users)
- Discussed multiple AWS credential support and bucket permissions

### Transcript

00:32 Sid Mehta
Hey Andrew, how are you?

00:35 Andrew McCann
I'm good.

00:36 Praveen Palem
Hey Andrew. Nice to meet you.

00:38 Andrew McCann
Hey, nice to meet you.

00:42 Sid Mehta
You're the SSO expert and Imari, we understand?

00:46 Andrew McCann
Yes. Alright, cool.

00:50 Sid Mehta
I think we're just waiting for it. One sixth or we're just waiting for Danielle.

00:56 Andrew McCann
Danielle? Yeah.

00:57 Sid Mehta
Danelle Dan, sorry. Okay.

01:00 Praveen Palem
While we're waiting, I guess Andrew, anything that you need us to address from an S or login standpoint?

01:07 Andrew McCann
No, everything seems to be working fine so far. Perfect.

01:11 Sid Mehta
Sounds good. I guess you also logged into the platform as well, right? You're an admin as well?

01:16 Andrew McCann
Yes. Perfect. I'm an admin but I might make like Danelle an admin so that she can manage users as well as me and I can just do it to backup.

01:30 Sid Mehta
Got it. Alright.

01:32 Andrew McCann
I'll discuss that with her separately.

01:35 Sid Mehta
Yeah. Yeah. Actually yeah, may maybe based on what I showed today, that'd also make, it might make a lot of sense.

01:42 Andrew McCann
Okay.

01:42 Sid Mehta
Weird. I, she has to join and I admitted her but didn't go through.

02:10 Praveen Palem
Hi Donelle.

02:11 Danelle Cline
Hello.

02:14 Andrew McCann
How are you doing?

02:14 Sid Mehta
Good weekend.

02:15 Danelle Cline
I like Your background saver. That's very apropos proposed. Yeah.

02:20 Praveen Palem
Thank you. Very thanks.

02:23 Danelle Cline
It's like I'm just wanna be home next to my fire instead of working.

02:29 Praveen Palem
Oh, hopefully it's not too distracting.

02:31 Danelle Cline
No, it's fine. Alright, I need a vacation. Can you tell Good morning.

02:38 Sid Mehta
Yeah, good morning to you and yeah, almost to the holidays as well. So just super near. But yeah, we just thought we'd just sync today, just kind of see, it sounds like you guys first step was to log into the deployment so that's great you can do that. Wanted to just then also check how you've been on, like the tutorial that we have on how to get your S3 back data into the platform. Any questions that you might have.

03:01 Danelle Cline
I don't know if you've had the time to do it Or, I haven't had time to do that, but I have my data in an S3 bucket. Okay. I now, I think I have permission to do it. I don't think I had that till this morning. Perfect.

03:13 Praveen Palem
Can I start recording for Laura?

03:15 Danelle Cline
Yes, yes, please do.

03:18 Sid Mehta
Yeah, yeah. Okay cool.

03:20 Danelle Cline
So then just to reiterate, so yeah it would just be following, Did we just walk through the upload, I mean the addition of the data set or is that, that needs, it needs to be done through the API, is that right?

03:35 Sid Mehta
Yeah, so we have like two options here. I would recommend starting with the SDK, so like basically you'll go here, you'll configure, you'll, this is where you'll input your credentials file to the deployment and then this is for you know, the entirety of the deployment. We'll have these credentials and then I would then follow these steps on how to get your API key set locally and all that type of stuff of how to connect to your deployment. And then we have some checks and balances in here as well. Like there's a way to test your API connection so there are checks within this guide letting you know like before you move on to step this next step, this step should work. And then you would set these same cloud credentials locally as well. We recommend to do that as well. So you would set this AWS access key ID act and all this other stuff. And then the last thing is then the script here that's super easy. That's just you copy and then the input of this is like generally an S3 bucket. So I assume you have like an S3 bucket that has like a folder of images or whatever data you're stored it and then yeah, you might need to change this to jpeg to your format and then yeah, it should just be as simple as that. And then we do have recommended as like LA last step per any data set that you ever upload, which is that you compute the metadata on the dataset. So like what's the image size and all that type of stuff. It just helps for helping the app perform better and render your data faster. So yeah, that's kind of the steps that I would recommend to do. We have this other section, but I think I would re generally recommend long-term to work with the SDK first just so we can get, make sure that you can do the API connection and all that other stuff as Well.

05:04 Danelle Cline
Yes, yes. So I have a couple questions. I've been using the pre community version.

05:13 Sid Mehta
Yeah.

05:14 Danelle Cline
And it's, it's first of all, it's a really great tool. I know I'm speaking to the choir here, but I have loaded several different data sets in it from other projects and immediately found some interesting observations. I'll just say not, not, not just errors in the data but cases where things were ambiguous and it really helped highlight that. So I'm excited to, to use a tool for this project so I understand how to write a script to load data and metadata about that, like the samples, the labels and, and things like that. So I have a script to do that. Yeah, and I'm assuming that same script can work with the, the enterprise version, is that right? It's all compatible. Yeah.

06:07 Sid Mehta
It's gonna be very similar. The main difference is that you're probably using local file packs and here you're just be using S3 file packs. So you should be able to use the exact same script and then that's the only thing that you'll be changing. So the, just make sure when you're doing this. So a lot of times what people get confused is that they're using the open source SDK. Yeah. And then we, for the enterprise, you're actually gonna PIP install a different SDK.

06:31 Danelle Cline
Oh, okay.

06:31 Sid Mehta
It's the enterprise one. Very similar.

06:34 Danelle Cline
Okay.

06:34 Sid Mehta
Almost exact same, almost to a fault. But the main difference is that the enterprise SDK will work with these cloud file paths. So that's like one I one thing to every customer. It's almost like a R of passage from every customer who goes to open source to enterprise. They do get into this thing where they like are trying to use the enterprise SDK and do enterprise stuff with the open source SD K and they flip back and forth. So there is a quick check and it's actually in this guide is here, but if you the, but if you do 50 import, 51 do management as FOM, that's like a quick test to make sure that you're using the enterprise SDK 'cause this is not available in the open source.

07:10 Danelle Cline
That's good to know.

07:12 Sid Mehta
Okay, That's a good test. And then this FOM test API connection is also like a good sanity check. So yeah, you should be able to use that script. Hopefully it looks very similar to this one, but if not this is like a good starter one that we have. But yeah, it should be very easy. And then you can also, that's also fair game to send that us that over in case something isn't working and then Pravin will be able to kind of, to take a look and debug that way. But in general there's that also what we can do as well is that you can take stuff that you've done in open source SDK and then you could export it to the 51 format and then you can then import it to your 51 enterprise deployment. So you'd be basically taking, now the question there is like, okay, what do you do with the file paths, right? We also have a way to like where you can upload file stuff through our SDK. So you have a dataset in enterprise it won't show because you know, it'd be looking for local file paths. But then we do have a method where you can update the file PLAs and they'll update everything to S3 as well. So that's also another option if you did a lot of work you felt like already, and then don't wanna just redo it 'cause I, it sounds like you will have to move that data back into S3 anyway, but if you kind of wanna do that through 51, we can also show you how to do that.

08:24 Danelle Cline
Yes. I, I think that, that, that's potentially on the roadmap here. Okay, cool.

08:30 Sid Mehta
So yeah. Yeah. So my recommendation would be kind of go through this first one, just make sure the S3 and all that stuff works. Okay. Once that's working then we can show you how to like export from OSS and then import to 51 Enterprise. And then what's the command you'll have to do afterwards to upload local file pads to S3 with the SDK. Okay, Got It.

08:50 Danelle Cline
That's great. So the other had was thank you for that information. What in, in our SE account, we generate credentials that expire in 12 hours for security reasons. So I assume that's fine 'cause I'm just gonna be uploading data and then I'm done, right? I don't need to have persistent credentials.

09:17 Sid Mehta
Oh, that's a good question. So I feel like the credential, because if the credentials would need to be persistent because we're basing the credentials to render the data. So if the credentials don't exist, okay, then, then I then you might not be able to see your data.

09:30 Danelle Cline
So, so we need, yeah, Generally we have to send non expiring credentials for this. Yes. Okay.

09:38 Sid Mehta
Yeah. Yeah. You would want the credentials to actually, yeah, you would want it.

09:41 Danelle Cline
How Do we, how do we do that? How should we do that Andrew?

09:47 Andrew McCann
I would actually recommend, instead of creating non expiring credentials, just create a credential that has like a really long lifetime, like a year and then just have that be part of your standard procedure.

09:55 Danelle Cline
Like once a Can I do that? Do I have permission to do that In AWS?

09:59 Andrew McCann
I'm not sure.

10:01 Danelle Cline
Oh, okay.

10:04 Sid Mehta
Yeah, that's a good call out though.

10:06 Danelle Cline
Yeah, you would want, I think, I mean There's a way to rotate them out There is, I think that's, That's another thing that we could do.

10:12 Andrew McCann
But it's, I, yeah, yeah, I think long, long term, ideally we would wanna switch to a system where it would like be automatically rotating keys, but I'm not sure what exactly that would look like.

10:24 Danelle Cline
Okay. So there's a little work to do there to make Yeah, yeah.

10:30 Sid Mehta
Persistent.

10:31 Danelle Cline
Okay. I'll talk with her, the person that's our A WS account to see how, how best to do that.

10:39 Andrew McCann
Yeah, that's kind of, we should bring Travis in on that because he is more familiar with how ation works in AWS than I am.

10:46 Danelle Cline
Yes. I mean I, yes, definitely because we wanna, we, we wanna be secure about this and not, not that any of our data's really, there's not an issue with getting it that this particular day to get it on the open, but it's the compute and everything. We don't wanna Yeah.

11:06 Andrew McCann
Have this, there's, there's a couple different ways that we can go at this. It just depends on, you know, what we need and what our capabilities are with the software.

11:13 Sid Mehta
So Yeah, so you will put the credentials here in cloud storage and then Yeah, it's kind of, you'll put the AWS credentials here. It can be the INF file or you can do it this way. But yeah, I, I guess it would just be tedious, right? If you had rotating ones every 12 hours, it would be tedious to like update this, all this. So yeah, I think what you can, whatever you can do to make it so that you only do this once and send and forget is probably, I think the best way to Do it is there an API to it.

11:40 Danelle Cline
So if we wanted to do rotating credentials, we need to have programmatic assets to it.

11:44 Sid Mehta
Yeah, that's excellent question. Can we up, can we upload these via a PII Believe you should with the 51 management, that's something Pravin and I look at. I believe you can where you could do this programmatically. Yeah, I, I, yeah, I believe that might be possible. Yeah.

12:04 Andrew McCann
I'll double double Check. It looks like you support OIDC in here and I think like that would be the, the proper way of doing it with like AWS is like doing OIDC between you and AWS, but it looks like you just support access keys. So we would have to have some kind of API based way on your end to upload new access keys and then we could write a piece of software that would, you know, on a, you know, regular basis connect your API upload a new API key time, a new time-limited API key. And another thing too is that we would also want to clearly scope out the permissions that this API key has. So it has no more than what it absolutely needs to do its job since will be a relatively long lived API key. So do you have documentation on, I forget the name of what it calls an AWS, but basically like the permission set that we need to assign to the access key in AWS I?

13:06 Sid Mehta
Yeah, I think at, at the, I'm not familiar with, I I, we use GCP internally so I, I can see what it is, but essentially we would just need read and then also potentially write access to these buckets. But I'll, I'll try seeing if we can find what the internal, like actual S3 permissions are that we need and, and send it.

13:24 Danelle Cline
It's Very similar in AWS Yeah, I'm sure we can figure it out.

13:28 Andrew McCann
Just like if you have any documentation on like, hey here's like our recommended like baseline kind of thing.

13:33 Sid Mehta
Yeah. Yeah, I think we can do those and yeah, I did see you could do with the 51 management, SDK, we do have these ad credentials, cloud credentials thing. So if you wanna do it by SD K, you can still would recommend it possible to do the, just if you can, if it's possible to the one time set it, forget it. 'cause even, yeah, I'm just trying to like even if you were to do it with the SDK, would you still like wanna do it every 12 hours or would you want to make it still a bit longer?

14:01 Andrew McCann
I don't know if we'd wanna do it every 12 hours. Okay. But you know, maybe like a week or something like that.

14:05 Danelle Cline
Okay.

14:05 Andrew McCann
And I think Danelle it's probably fine to have a longer lived token if it is tightly scoped to only access the stuff that it needs.

14:13 Danelle Cline
Yes.

14:13 Andrew McCann
So like if we scope it down to like just the one S3 bucket that has your data in it and we limit it to only the, you know, read write permissions that it needs, then that would be acceptable to have a slightly longer lived token.

14:27 Sid Mehta
And on our end we also do allow you at in our end, right, if you want to just also say that it's only these buckets within this key, we do have that, but it sounds like you might want that security on the S3 side of the token rather than on me.

14:39 Andrew McCann
Definitely, yeah. It'd be like for the longer lived access token on the S3 side, we'd want to enforce those controls on the S3 side.

14:46 Sid Mehta
Got it, got it. Cool. So I will send you this function or, and a follow up. Pravin can send you this credentials and then we can also ask internally for some of our more S3 experts within 51 to be like, what exact permissions do you usually need? Do we need to give on this, on this key?

15:05 Danelle Cline
Cool. Great. So thank you I, those were my main kind of administrative questions.

15:14 Sid Mehta
Yeah.

15:16 Danelle Cline
I do have a question now that I've used it a little bit with some data sets just generally about best practices for loading and the use of names, tags and l and and and labels. Sort of walk me through a little bit how, how people are using tags versus labels.

15:44 Sid Mehta
Yeah, so labels now, I think the main advantage of labels, right? Labels are generally like used for classification bounding box types, key points, right? We support a wide variety of labels. Now if you have labels as in ground truth labels and model, and then eventually you'll train a model and then you wanna input model prediction labels. You should probably be using the labels field because eventually down the line then you can use our model evaluation capabilities, which let me go to a better data set here. If I go to demo, right? So like let's say eventually you have a data set that has ground truth labels, but it also has model prediction labels. Like this one here, there's a lot here, but we have, okay, you can kind of see we have best model, we have in ground truth labels all on this dataset. So if you, if you use labels then you can eventually use our model evaluation functionality, which you come here and you say, I want to evaluate this model. You give it a prediction field. So this would be your model prediction field that you uploaded and then you give it your ground truth field and then what you get and then, oh that's nice. And then run all this stuff and then what your results, and I'll show you what the result is, which is this thing right here where you can get like all the metrics like F1 scores, precision recall, and then you can filter it by class as well. So you can see like how your model's performing across different classes. So this is why like if you're using, yeah, yeah. So if you are using like actual stuff like this, I would recommend to use labels. Obviously we have primitive fields as well, but like we, so if you're have like a string that you'll eventually want to evaluate, right, like a certain class type, then I would use classifications rather than a tag. Also with the big difference between tag, right? Is that you can have for one image, right, you can have multiple tags, right? So tags are like, whereas like labels, you can only have like one label out of time. Does it make sense? Like if it's a classification, right? Good or bad, right? It can only be good or it can be bad tags. Technically you can have a good tag, you can have a bad tag and then it's on you to make sure that when you add the good tag or, or you don't have multiple tags, right? So that's kind of where I, I generally, personally when I'm doing like most of this stuff, I, I've rarely used tags. Like I use them, I don't use them too much long term. Like I might like look, I might do something for a tag where it's like, oh this is like an annotation mistake.

18:03 Danelle Cline
So I tag it as like, hey, So that's found, that's how I'm finding the tag useful is to sort of say this is an error. So lemme step back a little bit and just say we have, for each of our ground truth labels, we have a unique ID and that that IE ID is referenced back to our internal database and I don't wanna, I don't wanna lose that information. So I need to be able to reconcile a change made in voxel 51 with my internal database. So how will I know if something has changed within a label? So if I look at a ground truth and that gets revised.

18:54 Sid Mehta
Got it. Yeah. So you would, so basically you're saying the scenarios like let's say I have this ground truth here and I want to potentially the label gets changed somehow some way. Would you, now we do have some annotation capabilities that we are bringing to the platform soon, but like how do you expect this, these label To change?

19:11 Danelle Cline
I don't expect the ma I don't expect any boxes to change.

19:15 Sid Mehta
Okay.

19:16 Danelle Cline
I just expect that we're, we're gonna quickly discover where we have errors in our annotation. Okay. We need to correct those and I need to know which, what has changed so I can keep, keep the databases synchronized.

19:33 Sid Mehta
Yeah. Got it, got it. Okay. Interesting. Yeah, so we have, yeah, so we have a lot of customers build this, it's called like a sync pack normally, where like they have this internal database that's their all knowing database. Yeah. And they load from this database to 51, but then sometimes changes are made within 51 and then they wanna write those back, right. So gen, so generally what I've seen is that they eventually make like a plugin for this. We can talk about, I was gonna talk about plugins, but then it's something that, 'cause it's so custom to everyone else, but what they, of course, yeah. But what they do, so what they'll do is that they'll have like a plugin that they've written that like, you know, fits their database, their data structure and they'll like come here and then it'll just be like, I, I don't think we have an example here, but it'd be like rewrite or like sync back or they'll call it like the sync back plugin and then they'll run it and then it'll update and it'll connect to their database and it'll just run updates. Right. So it'll go through and say like, what, what has changed? Now, I don't think as of right now we, we don't have like really granular audit. Like we tell you when like something was last modified, but we don't tell you exactly what. So I think like right now you would still have to find a parse through everything and just make sure everything syncs is likey back properly. But like yeah, this would be something where like once you get, this would be like a good first plugin to write. 'cause like that's like one thing that we teams do is that they have this, they start with 51, they get onboarded and eventually we talk about plugins and how they can build these extensions.

20:56 Danelle Cline
Yeah. I mean it wasn't very hard to write a script to download and then update.

21:00 Sid Mehta
Yeah.

21:01 Danelle Cline
That was very straightforward. But I did not, I did not change the ground truth. Right. I did it by just change, just tagging them.

21:09 Sid Mehta
Got it.

21:10 Danelle Cline
Was able to tell, okay, there's a tag on this. The tag is different from the ground truth. Yeah. Therefore 'cause because you know, you don't wanna update thousands, thousands of things just so, yeah.

21:21 Sid Mehta
Yeah.

21:22 Danelle Cline
I mean, so it's a plugin but there isn't sort of a, a plugin that can run in the background asynchronous when a change is made. That's it. It's, it's sort of an action that happens by user.

21:33 Sid Mehta
Yeah. Yeah. Right now I, I think what you're describing, it's something we would call like a, what is the word? Like a web hook. We don't have like a web hook for it that's something is trained and triggers Something that Okay. Yeah. Yeah.

21:45 Danelle Cline
But we That's fine.

21:46 Sid Mehta
That's fine.

21:47 Danelle Cline
I just, it's it's just worth kind of sussing out.

21:49 Sid Mehta
Yeah, yeah. So normally some people will do is that they'll just run it like once a week or like once or whatever cadence they want and then it can run like run in the background in the platform. But yeah, it's definitely something we like and it's good that you have a script that kind of does something like it and yeah, maybe the fact that like the samples are tagged, then you kind of know, okay, only the samples that are tagged are the ones I need to go and update. So, and then that's what your sync back kind of plugin can do. We can look at the ones that are tagged bad or like need to update, go through those, make those updates in the database and then see that The last update time is sufficient.

22:21 Danelle Cline
Yeah. Yeah. And that might be cleaner because then it really fully uses the tool. Yeah. And, and that that and that would be okay to, yeah. And I, I, I don't wanna use it inappropriately.

22:33 Sid Mehta
Yeah. Yeah. I'll have to see whether we do the sample level when it was last modified that I know for the dataset level. But at the sample level I have to see if we have the last Modified data. Okay. If you could confirm, that would be great.

22:43 Danelle Cline
Yeah. So very cool. And then I imagine what we'll probably wanna do pretty quickly, I, I think I can get the data loaded today, but we'll probably pretty quickly want to, one of the things as I understand it, the the, the enterprise lets you do the embedding Yes. Within the tool. So a little bit, Yeah.

23:09 Sid Mehta
Yeah. So that's a, that's a good segue to maybe what I wanted to talk about was like once you get to that about and so you can learn a little bit more about the deployment. So yeah, like for example, this data sits right here. Embeddings is like super popular thing. So once you get data and what's interesting is that you can do embedding. So you'll go here and then you'll see embeddings here and then you click plus 'cause you want to create a new embeddings and then you'll get this kind of form that you have to fill out. So you have to give it some random key. So this can kind of be like example three. Now what's interesting is that you can run embeddings at the sample level but also at a patches level or at the label level, right? So let's say if you have bounding boxes, you could run it on embeddings there. So it would, it would, do you, do you guys use bounding box label types? I forgot or Yeah.

23:55 Danelle Cline
Yes. For other projects We do.

23:58 Sid Mehta
Yeah. Yeah.

23:58 Danelle Cline
And so you think about this like the entire thing is abounding box.

24:03 Sid Mehta
Got it, got it. Yeah. So you could choose to run it at the data set level at the sample level or you could do it at the patches level. It's your choice and then you would then choose a model. We have a lot of models here to be honest. We're trying to actually like reduce it. 'cause like some of these are like a little older and whatnot. So we're trying to make it easier. I will send you, Pravin can also send you a new blog post or ML research team did on like some findings that we found about like embedding models and how good that they are. So I will send you those. But like, and some of these mo yeah, so we have like, does It have to be in the brain key?

24:37 Danelle Cline
Can we upload our own?

24:39 Sid Mehta
Oh yeah, yeah.

24:41 Danelle Cline
These models are pulled.

24:42 Sid Mehta
Yeah. Yeah. So these models are pulled from our model to do. So I would recommend, I generally recommend at least trying one of these ones and if they don't work for you, then I would go through the, you know okay of yeah, yeah, try it out. So like I think a lot like dyno and clip I think are the most popular ones people use. Yeah. So you can try one of those and then you'll give it like a dimension redaction. I think like UAP is like perfect. And then this is one of the things that I wanted to talk about, which is when you get, now when you schedule this, you can do two things, right? So you'll see execute here, execute will make it a synchronous operation. So you can imagine that computing embeddings is like expensive, right? And especially depends on how much data that you have. And it also how many patches you are running around. So what we highly recommend is rather than execute with your deployment, what you got was like two, what we call delegated operators. I think maybe AZ might've explained what this was for you, but it is basically like how you can schedule this operations in the background. So what you'll do is that I'll click schedule here, actually let me set a model so that this doesn't actually fail and I'll just do clip. So I'll schedule this application and what it'll do is that it will now run this thing in the background and I should see it here. I can go and see exactly what I ran, I'll see the input, right? These are the input values I gave for it. And then it'll just run in the background and then you can still do whatever you want in the app. If you could execute what happened. It's that it's gonna be a synchronous operation and the app will kind of hold and we kind of don't want to do that for a very long running task, which embeddings could be, right now this is a CPU backend, but it's possible that we'll be bringing potentially a GPU backend really soon. So we'll let you know what that, what, what, what you would need to do to opt into That.

26:34 Danelle Cline
Yeah, that would be cool. But let's say for example, that makes perfect sense to me. You'd want background, but let's say you wanna sort of zoom into a cluster of things that are very similar. Yeah, maybe it's a couple hundred and I just wanna sort of look at that, that that might be okay, right?

26:54 Sid Mehta
Yeah, I would do it like yeah, if you wanna like, so you, so that's another good thing is that like, that's a good point. So let's say like right now I was running this on the entire dataset, but I can also do something where like I like only select a few images or I think we've talked, you're familiar with views, you have views as well, which are subsets of your data. So you can choose to run embeddings on either. So if we go back to the form now it's gonna ask me do I want to do it on the entire dataset or just this view? And if I had selected samples, it would also say like, do you only wanna run it on these like five or 10 samples?

27:25 Danelle Cline
Yeah.

27:26 Sid Mehta
So you can do it at that. So yeah, if you wanted to just do that, like execute for like less than a hundred maybe I'm always the billion though, just to do it in the background, just you know, again, 'cause also for example, the Dyna model that I was telling you about, it's a BC model so it'll take a while even for a bit, right? So in general I would recommend to do that just because you'll probably wait the same amount of time to be honest and at least you can do other stuff while you're waiting for it.

27:49 Danelle Cline
So yeah.

27:50 Sid Mehta
But yeah, and then just so you know with your deployment you can run two of those at the same time. And then the third one, 'cause you, you bought with your deployment it came with two vpu, the third one it'll just wait for the other, one of the other two jobs to finish and then it'll start the third one. So you can schedule how much you want, but it'll only run two at a time with your current deployment.

28:10 Danelle Cline
Okay. Yeah.

28:11 Sid Mehta
Got it. So that's one thing I wanted to talk about, which is delegated operation and yeah, it's great that you are already thinking about embeddings and yeah, that's like one of the most popular ways we've done it. And yeah, if that model doesn't work for you, then we can kind of talk about how you would want to bring your own model and then visualize that within the platform.

28:28 Danelle Cline
Well the only thing I would say is that we've done fair amount of, of evaluation, fine tuning of the dyno models and the, the model, the Facebook model with the eight block size pixel block size really works the best on our data because it is so small and grainy. And so if that's not in the brain, the model zoo, it would be great for your team to add it.

28:58 Sid Mehta
Got it, got it.

28:58 Danelle Cline
Yeah, we Can know it's a complication, probably more expensive to run it, but it really gets at the more details in the features that We got it.

29:05 Sid Mehta
Got it.

29:06 Danelle Cline
Yeah. We can also run offline and you know, yeah go through this, but then there's a little bit of work, if I understand it, you know, we, we can upload, because I've done this through the, the free version, computer embeddings upload, we can do the same thing here.

29:22 Sid Mehta
Yeah.

29:23 Danelle Cline
An offline Upload, but then it gets a little cumbersome, right? When you're interacting with a tool, creating a view and now you wanna run it on the view, then that's where the integration I think would be nice to be able to run.

29:36 Sid Mehta
Yeah, I Agree. Yeah. Yeah, I agree. Yeah, we can kind of show you how you would wanna maybe add the more model or like yeah, we can talk about how to do that. So cool. Yeah. And then, yeah, it seems like you're, it's already great 'cause yeah, this is one thing I think everyone who uses 51 do, they should run our beddings workflow. So it's already great that you're thinking about that. And yeah, I think like that and then also the evaluation thing or things I would always recommend every, everyone who's working with 51 should use those two features super useful 'cause yeah, like I'm not sure if I even showed, showed it properly when I was showing you, but like for the evaluation stuff, you can get down to the class level of like if we go here class performance and then you can see like, oh well bicycles and they'll show you all the samples that has the bicycle class and why I may be performing less on it as well. Mm. So yeah, so all more reasons to get your model predictions and ground shoot labels into 51. Yeah, that's that's cool.

30:31 Danelle Cline
And is this is only available in the enterprise version, right?

30:36 Sid Mehta
I think you can run eval runs in 50 in open source. I just don't know how the UI is for it, like whether you can do it through the ui. I think you can mainly do it by SDK, but the visualization should be there.

30:47 Danelle Cline
But yeah, So that could help with our development.

30:49 Sid Mehta
Yeah. Yeah. So And then one more, oh sorry, go ahead.

30:53 Danelle Cline
Go ahead. No, please.

30:54 Sid Mehta
Oh yeah and then I was gonna say you can also compare two models as well. So you have eval best and then eval first. So we can compare side by side. So if you have like, you know, one ground truth prediction but two model predictions here, right? You see have best model in first model, you can actually, and I don't know why it's taking so long, but you can actually, yeah, see side by side how they perform. And again, all these numbers is there. And then also we have this thing called scenario analysis. So the way I like to think about it's that you have a data set but then that data set, right? If you think about views, you have like different metadata, right? So like for example here we have data that's taken, some of it is taken the day versus in the night. So what you can do is that you can define based on the data that you have on your data set just to kind of create subsets of your data, right? So in this case we have data that's taken the daytime versus the night so that we can compare like, hey, does our model perform better in the day versus the model in the night with your use case, it might be possible like the location of where the data was taken might be, it might vary, right? Maybe like some data's taken in one ocean, some taken, some data's taken in another ocean. So are you for some reason worse than the arctic ocean than you are in the Indian Ocean?

32:05 Danelle Cline
I'm Absolutely, yeah.

32:06 Sid Mehta
Yeah. So like some, so you can kind of with a scenario analysis feature, that's what it is that it allows you to like do model performance but go one level deeper and see like, okay, which subsets does my model actually like suck at, for lack of a better term.

32:20 Danelle Cline
No, this is terrific. Got it. This Be really helpful. Yeah.

32:24 Sid Mehta
Yeah. And again, it's a very vast tool, so we like to go, you know, step by step, This is, this is great. So when you go to like, I think embeddings visualization is like, you know, a good first step and then once you get there you get your model predictions in, then it makes sense to do model evaluation and whatnot. So. Cool. But you had one more question that you wanted to ask before I was ranting about mono matters.

32:44 Danelle Cline
No, no, no. This is all, this is all really helpful. We touched a little bit on this in our earlier calls about some tricks to constrain, excuse me, the ground truths because we, we've got our labels are really complicated sometimes and it's really easy to spell something wrong. And so tell me, walk me through that a little bit. If I've got somebody looking through the data and I want them to add to clean it or add an I want constrained labels, can I do that? If, if not, Okay, so one thing that we Like where we check the labels.

33:29 Sid Mehta
Yeah. So one thing that we, now I'm wondering 'cause so we did release in the newest I I don't think it might be available under deployment yet. 'cause right now it's like an alpha feature, but we did, but it might be worth it for your use case where like, so what we are giving now people is the ability to annotate within 51. So you, you'll still need to bring, define a label field, bring in your labels. But now what I can do is that if I have a bounding box, or right now we're supporting detection labels and classification labels, I can move this label around, I can change the, oh whoops, sorry, this is a bad example. Gimme one second. I think it's on this one. Okay. Yeah I can, so I have these labels, I can change them, I can change the labels class and all this type of stuff and you know, they could save this and it'll actually change the label field. So we have these like annotation teachers features in the tool and what we, and then how this works. Let me actually show you how the, how how you get to this. So like we, first of all, you can let me know if you want to try this feature right now.

34:33 Danelle Cline
Well You know that I think we would like to try it but we need to be able to do it on in maybe in bulk. We can't step through each image.

34:42 Sid Mehta
Yeah, okay.

34:43 Danelle Cline
Half a million. I mean I think we might be able to interactively do it through the embeddings view.

34:49 Sid Mehta
Yeah.

34:49 Danelle Cline
In bulk change through that.

34:51 Sid Mehta
Yeah. Yeah. That that's usually what we recommend is that you start in the embeddings view, you find like what are the samples that you want to focus on? And then you can, like right now we don't have like bulk changing with this. If you wanna do bulk changing the best ways to like add some tags that says these need to change and then you go one by one on the ones that do need to change. But so bulk of you doesn't do that. But like on an individual sample level, like maybe some, this is I guess something to show you. So let's actually, let me actually start from scratch. So like how, how would this work is that you would go here and on your dataset and you would see nothing, right? Because what you need to do is that you add a need to add, you need to tell the tool what schema, like what, what do I want to allow the people to annotate? So you go here and then we're gonna make this easier, but you basically go here and what you'll see here is all your fields that you have, whoops, let me, yeah, you'll see all the fields here that you have. And then again, you have to have this field on the dataset. We don't allow like the creation of entirely new field. The idea here is that you can create and have a field on the data set and it'll scan all these samples. So it'll scan it and then it'll create the schema for you. So this is like what I wanted to show where it's like okay, you have these classes and they're very, and you can kind of define like, hey I only want you to live in these classes. This is only what you should be able to change. So that's why I was thinking this might be good for your use case because very specific.

36:16 Danelle Cline
Absolutely, yeah.

36:17 Sid Mehta
You can and fields on the data on the de detections we call attributes. So you can also define your own custom attributes as well. So if you wanna put your ID identifier as a field here, you can do that as here, you can, you can also do that as here and a render like this, you can also say like what type of the input should it be? Should be a select input. Should this be something someone can type in? Right? You can kind of define it like that. Once you do that, you promote it to an active field and once it's on the active field, that's when you'll see what I saw before and you can change and notice I can only change this labels to only a select few, right? I can't just do willy-nilly what I want.

36:58 Danelle Cline
Yeah, that would be so helpful.

37:00 Sid Mehta
Got it. So would you be interested in us turning on these annotation features for you?

37:04 Danelle Cline
Absolutely, yes.

37:05 Sid Mehta
Okay.

37:05 Danelle Cline
Got it.

37:06 Sid Mehta
Got it. And then just again we're, I'm trying Be beta testers too.

37:09 Danelle Cline
I mean we're, yeah, yeah. We're all, you know, we We Trying new things and fail. Yeah, yeah.

37:19 Sid Mehta
We just want everyone to know it is an alpha feature so there might be, you know, some kinks to it.

37:22 Danelle Cline
Well, And then, and you know, I, I realize that we all need to flexibility a model little soapbox here in annotation. You don't always know. It depends on the problem, right?

37:34 Sid Mehta
Yeah.

37:35 Danelle Cline
I'm trying to tackle and so we don't always know ahead of time how we need to label things and that's part of the, we need flexible schemas, right? Yeah, yeah. We need sometimes unknown or noise or you know, try this or whatever and, and that's so important. But we also just don't wanna have to spend a lot of time cleaning up when we're done labeling the data. Yeah, makes sense.

37:58 Sid Mehta
And you can come back at any point and change the schema and it'll persist throughout for all the samples. And then just so you know, you can also create new detections and new classifications as well with this as well. So if you wanna draw a new bounding box, you can also do that as well in this thing. So pretty good.

38:12 Danelle Cline
Okay, cool.

38:12 Sid Mehta
Yeah, Pravin and I can work on this feature getting this enabled on for, for you guys just so you can play around with it. And then that might be helpful 'cause this is an alpha feature. Our docs are also on Alpha, so it, I might need to send you like a Google Docs version of the docs that are going to be, but eventually this will be on our normal docs. It's just like I said, alpha feature. So you know, docs are also an alpha.

38:37 Danelle Cline
I understand.

38:38 Sid Mehta
Awesome. And then the last thing I wanted to just show you about your deployment is the whole concept of like plugins and how you upload them. So just in general we have like kind of three versions of plugins. I would say in 51. One are like, and we use plugins to make the platform more extensible. So oftentimes what happens is that a new feature will start as a plugin and then once everyone is like, hey we want to use this, we eventually just like then kind of use our plugin favor to in integrate it and then it just becomes available built in house. Nice. So we do have like what we call, and I'll show you this repo, and again we'll send all this information in Slack, but we have our 50 ones plugins repo where we kind of have the ones that fif the 51 team manages. So if you go here you'll see plugins and then it'll kind of just be like, and then with within these plugins there might be a couple different operators and I'll show you how you can bring those up as well. But these are the different plugins that we have. And I would say the ones that I recommend to install are annotation, brain dashboard io and u utils. So it's a lot the, it might be a lot, but again, we'll, we'll re we'll send, we'll send you some of this stuff, but those are ones that I just recommend kind of everyone deploy. Again, we're probably gonna make these built-in ones soon, but you can just install those. I can kind of walk through each one, but brain kind of will add some of the more functionality, right? So computer embeddings is there, but like compute, similarity, uniqueness, hardness, all that functionalities installed with the brain plugin. And then we also had the annotation plugin as well. So if you, this one integrates with like stuff like CVA label box, I don't know if you use any of those tools, but if you do, that's the one that we would recommend to install. Do you use any labeling labeling tools like those?

40:21 Danelle Cline
The labeling tool we use is called Tater and it's, it's supports video and images.

40:28 Sid Mehta
Okay, Got it. So we don't support that one in that one.

40:31 Danelle Cline
At the moment It's, it's, it's no longer open source, so we're not really happy about that.

40:36 Sid Mehta
Got it, got it. Yeah, so maybe no need to do annotation plugin at the moment. 'cause we even getting that one, I mean you can build your own integration with it, but it's a lot of work, so I wouldn't recommend it at least.

40:48 Danelle Cline
No, I mean it and it, and it, so we have, so we have such a diverse data set too, trying to build, trying to find an annotation tool that fits it all. It's, it's pretty hard.

40:59 Sid Mehta
Got it, got it. Sorry, go ahead. Ferin. Yeah, I think you're on mute.

41:03 Praveen Palem
Can you say what to that is again, I'm, I'm, I'm trying to write my Notes.

41:08 Danelle Cline
Tater, P-A-T-O-R-P-A-T-O-R, like Tater talk.

41:14 Sid Mehta
Oh, okay. Well now I'm hungry, so cool. Okay, so annotation one brain, a hundred percent recommend because if you see anything in our, our docs about our brain functionality all like the, and Brain, brain sounds pretty helpful because yeah, uniqueness, duplicates, similarities.

41:35 Danelle Cline
Yeah, those are the kinds of things I think that would be really helpful for the teams.

41:39 Sid Mehta
Yeah. Yeah. So I, I would recommend to install that one dashboard is also like a really fun one. It basically allows you to create like charts based on your dataset. So.

41:48 Danelle Cline
Oh, very cool.

41:49 Sid Mehta
So if you go to like our dashboard plugin here, you can like, it can be really helpful to just get like, whoops, why is it, okay, so you can like say like what type of plot do I want to create? And then you can use data that you have that like creates these like plots as well. So I can say like, okay, from the time of like from the time of day I can see like day and night plots. Like I can like, you know, and this is really helpful if you ever wanna share like stuff about your data sets to other people like, and then you can create this as a plot and it's also interactive as well. So I think if I click on this as well, it'll show me all the night samples and just bring them up immediately. And you can also save this as like a workspace which you can kind of think of as like a, so, so you don't have to keep on recreating this, you can just go back to this as well. So dashboard I, I generally recommend just because you can create some nice charts which could be helpful when sharing to like, Well let's stay with that a little bit.

42:47 Danelle Cline
So yeah, creating a dashboard and then saving that as a workspace. We have some licenses for read only. Is that the kind of thing you would use that for? Yeah, yeah.

42:58 Sid Mehta
Perfect.

42:59 Danelle Cline
How then how do you share that?

43:01 Sid Mehta
Is there a short link or how a Yeah, so so what you'll do, so like let's say like I have these workspaces here, so this is what, oh yeah, someone already created this. Wow, this looks really beautiful. So like once, so then what you'll be able to do is that you'll just be able to copy and paste this and you can send this to Andrew. Okay. And then he should be able to open it and send it up and see the exact same thing.

43:20 Danelle Cline
I see. So the idea is it gets captured in a workspace.

43:24 Sid Mehta
Yeah. Yeah, exactly.

43:25 Danelle Cline
Nice. Perfect. Okay, cool. Terrific. This is great. Yeah.

43:29 Sid Mehta
And then, so it's cool. Yeah, actually we're going through a lot of the tool and then yeah, IO plugin and then I said tells plugin, they just have like some of the SDK methods that you can run as an operator and what I mean an operator, it's like some, so like for example, compute similarity. Once you install the plugin, which you'll want to do is that you'll come type it into, we call it the hamburger menu. Maybe that's not the best name for it, but it's this one here. Once you install the plugin, that's how you invoke it as well. So like when you want to eventually install your plugin for the sync back, that's probably how you would invoke it. It says my sync back plugin and then it'll run on your data set and then that's kind of how it works.

44:06 Danelle Cline
Oh, look at the brains. Those are cool. Okay.

44:09 Sid Mehta
Yeah, yeah.

44:09 Danelle Cline
Cool.

44:10 Sid Mehta
And then now I wanted to talk about, 'cause I was talking about with Andrews about your kind of access to this. I'm not sure if you're an admin right now, but I think it might make sense for you. So this is how you install plugins. It's very simple. You can see, actually, lemme go to my dataset. It's my deployment.

44:24 Danelle Cline
It's less, I think Laura and I definitely need to be admins.

44:27 Sid Mehta
Yeah, because, because then only admins can install plugins. So all these like plugins, I would like you to install. It would be nice if you do, and it's super simple. All you need to do is just, it's, it's it's zip upload. That's the easiest way to do it. Just zip up your plugins. And so like here, you'll go down, you'll download this repo, you'll zip this grain one into a folder and then you'll just upload it here and then you'll see that it's installed here. And then what you'll also be able to see are all the operators that were installed with it. So, oh wait, I'm not on, I'm on the, this one. So here I can see all the operators. Oh, I should be able to, whoops, my bad plugins. I can see all the other op. So compute similarity at similar samples, everything that comes in with this plugin. And what I can actually type into that hamburger menu is put over here. And I can also like do some permissioning on it as well. Like if I only want certain people to have access to certain plugins if you have that access there. So I think it makes a lot of sense for you and Lauren, if you're gonna be like doing a lot of this work and installing to install plugins as well.

45:33 Danelle Cline
So, And then, yes, so this is great. But, and now the invitation for users happens through administrators. Is that right?

45:50 Sid Mehta
Yeah, so I think we're not, so like, we're not so hard pressed that you can only join by invite. I think if anyone has access in your organization to their URL, they can Oh okay. Log and then they can, they'll be able to maybe sign in, but then you can, if they weren't supposed to do that, you can like remove them.

46:07 Andrew McCann
But yeah, maybe if you don't want keep, so this Is a, I'll, I'll chime in here. 'cause how we set things up is, in our SSO provider, we explicitly allow people to log into applications and if you're not allowed, you can't log in. Got it. So that's separate from like their permissions in voxel.

46:27 Danelle Cline
Okay.

46:27 Andrew McCann 51. But Right. For example, right now, Danielle, Danielle only you, me and Laura are allowed to log in.

46:34 Danelle Cline
Okay.

46:35 Andrew McCann
If anyone else tries to log in, they'll get a message from Duo saying you are not allowed to access this application. I have To.

46:43 Danelle Cline
Yeah. So if we have external collaborators, how does that work? Do we, Andrew, do we have to give you their email address?

46:50 Andrew McCann
That is an excellent question. For guest users. Do they have to do like SSO go through SSO?

46:58 Sid Mehta
Yeah, It'll still be the same thing where they'll have to log in, it'll be the same login thing. It's just, rather than coming as an admin or member role, they would be like a, what do you call it? They'd be a guest seat. So if I go here, like I, I have all these people on my deployment. That's The main, okay.

47:17 Andrew McCann
So all, all users, regardless of their role, have to go through SSO. You don't have like external users that we can, we can like say SSO is not enforced on these users?

47:27 Sid Mehta
No, I don't, I don't think, I don't believe, believe so.

47:29 Andrew McCann
Okay. Yeah, so Danelle, everyone has to have a ARI account to log into this regardless of whether or not they're an ARI employee or not.

47:37 Danelle Cline
Okay. I wish we'd known that before because we have external people of it, like at the, I think U-C-S-U-C-S-E that are supposed to log in. So Do they have like Use social accounts that's not gonna work?

47:54 Andrew McCann
Do they have like accounts, like contractor accounts or anything like that?

47:57 Danelle Cline
I dunno.

47:58 Andrew McCann
Okay.

48:00 Danelle Cline
We can't do social login.

48:03 Andrew McCann
We can, we have multiple SSO providers or just one.

48:08 Sid Mehta
This one I'll have to double check with our employment deployment and info team. If we were, if they can have two SSO logins. Yeah. So you would want the one that we currently have set up and then another one, right? Potentially.

48:23 Andrew McCann
Potentially.

48:23 Sid Mehta
Okay.

48:24 Andrew McCann
Google or something like that. Okay.

48:26 Sid Mehta
Yeah, let, let's, let me take that at the sync up with our in info team, whether that's possible. Yeah. 'cause yeah, we use AU zero. So, okay. Yeah, I can take that as a thing. Yeah.

48:37 Danelle Cline
Now I can make it unnecessary, complicated. 'cause I don't know, I don't think we have a lot of users but I, I'll have to check with Henry to see if the people that we wanna collaborate with are our, our, what's the right word here have col our collaborators, right. Where we have a collaboration agreement with them and then we, then we could potentially create an internal email account and this just sort of, and just have it, you know, just do that.

49:08 Sid Mehta
Yeah. So quick question Andrew, it sounds like the current SSO that you have is only for embar only this new one that you're thinking of adding, is that only for external only or could that be embar and external?

49:19 Andrew McCann
It would be for external only.

49:21 Sid Mehta
Okay.

49:22 Andrew McCann
Just so that, and that would just be so that we wouldn't have to create those accounts in our identity provider. Like I can create accounts for external people in our identity provider so they can log into applications. Yeah. It's just we have to get them set up with that account and everything.

49:37 Sid Mehta
Got, Yeah.

49:38 Andrew McCann
Yeah.

49:39 Sid Mehta
Alright. Let me ask our team, 'cause Yeah, okay. There's no, so it seems like there's no SSO right now that has like both internal and external. It's like one for internal, one for external.

49:48 Andrew McCann
Yeah. The way our SSO is set up right now is like you have to have an account in our organization to log in. We don't allow like just any random person with a Google account to like log in And I, that makes perfect sense to me.

50:01 Danelle Cline
I just, you know, I realize this is sort of in a little bit of uncharted territory. Again, there's not very many people in the world that know plankton. Truly.

50:10 Sid Mehta
Yeah.

50:11 Danelle Cline
Makes sense.

50:11 Sid Mehta
Yeah, yeah.

50:12 Danelle Cline
No, we gotta, we gotta get the maxis come in.

50:13 Sid Mehta
Yeah.

50:14 Danelle Cline
Would be good. Yeah.

50:14 Sid Mehta
We gotta get, yeah, yeah. No, we gotta get the max. Okay, cool. I, let me double check with our infra team and see what we, what we can think of.

50:22 Praveen Palem
I wanna, I wanna say everybody knows from SpongeBob, right?

50:25 Danelle Cline
Yeah, that's true.

50:28 Sid Mehta
Yeah.

50:29 Danelle Cline
Such an esoteric field. If I showed you the same animal from three different plankton recorders, it may look really, really different. And there's only a few people that, and there's also, there's been studies that actually among plankton people and there's a lot of disagreement between them about certain things. So it's, it's a, it's a challenging field and unfortunately a lot of them are getting really old and you know, the planet forever. So. Yeah.

51:00 Praveen Palem
You know, I was, I was, I was talking about plankton from SpongeBob. I don't know if you called that joke.

51:06 Danelle Cline
Oh, I didn't. Oh, oh Yeah.

51:09 Praveen Palem
I was saying everybody knows plankton from SpongeBob, Right? Plankton of course. Yeah.

51:16 Danelle Cline
I'm just, I'm too literal.

51:19 Sid Mehta
Yeah, that's good.

51:20 Danelle Cline
So It, whatever you, you know, I'll defer it to you, Andrew and, and voxel to tell, tell us what's best.

51:28 Sid Mehta
Yeah, yeah, we'll, we'll see what, yeah, we'll, we'll, we'll sync internally and then post in the channel that path forward.

51:34 Andrew McCann
So having Multiple SSO providers is not an option on the voxel side, you know, it is, it is possible for us to add external people to our directory and have them log in. Yeah. It's just more work on our part to manage those accounts. Makes sense.

51:46 Sid Mehta
Okay. Yeah.

51:47 Andrew McCann
Let's see what the best, that's Not, that's not, that's not an issue other than, you know, the overhead of management.

51:51 Danelle Cline
Yeah.

51:51 Sid Mehta
Yeah. Makes sense. Okay, cool. I'll see what's possible on our end and then we can see what the best platform Is.

51:56 Danelle Cline
I didn't understand that but that's okay.

51:59 Sid Mehta
Okay. So I know we talked about a lot about, but hopefully you kind of understand the deployment more. There's some next steps. I think the biggest one is making sure you can load that first S3 data set. Yeah. And then also then I would recommend to install the plugins and then run the embeddings digitalization. I feel like that's like a good north star to kind of aim towards and then, but yeah, you know, I think this is gonna be an iterative process. I think it also sounds like you already have want to eventually build like a plugin and then we can maybe further down the line or maybe back from the holidays. We can also talk about like developing plugin best practices as well. 'cause it sounds like you have a script, but then what, what we like to do is like some best practices on how you, you can develop these plugins, especially with 51 enterprise debug and whatnot. 'cause you can imagine uploading a zip file and you know, writing something, uploading a zip file and then expecting it to work is not the best development process, right? So we do have a way where you can like live code check and debug plugins and all that type of stuff. So I'll through the enterprise, but if I have, if I make, if I get it to work on the free version, is it true that it'll work in enterprise Or is most of the time, but sometimes those plugins, what they're doing is that there's like, they might be using environment variables, which then you would have to upload as like secrets. So most times, like, you know, a good plugin development is one that works on both. It's 'cause again, the file, the main difference is the file paths. But there might be just some like stuff where it's like, oh I'm, I'm using like for example, my C-A-T-U-R-L or I'm using something super like, like the database connections and whatnot and how you actually connect to the database. You might need to add those as like secrets here so the plugins can like pull and use for them. So that's probably the biggest change, but it's not a bad place to start. Right. Then it's just if you can get it to work there, then like the effort to do that I think would be like minimal. Like to just make sure that like the secrets and everything work in test. So it's not a bad place to start, but we can also show you how to do it with the 51 enterprise when we Get there.

53:50 Danelle Cline
Yeah. If there's a tools to help, I think that's always Yeah, yeah, there's, yeah, there's just a couple of stuff. So cool Examples really can accelerate this too. I don't think anything that we're doing is extraordinary in terms of, you know, workflows. Yeah.

54:07 Sid Mehta
Yeah. And the fact that you already have a script that does it is already like pretty good. That's often what we see the development is like, okay, you start a script and you're like, I'm tired of running this and, and this let me graduate to a plugin and you, we can also then like show you how to and then walk you through step. I like generally doing things step by step. It's nice to see the north star, but it's, you know, it's important to note that like, you know, it takes steps to get there. So we can walk you there. But I think I would first recommend like, you know, installing all the plugins that we have out of the box, making sure you like can use those and hopefully those are helpful and Yeah. Yeah. 'cause like some, that's often the thing people start like wanting to create plugins and then we're like, oh wait, we already have something that kind of does something like that. So how would you take that one, you modify it and then you use it for your use case for Pravin.

54:54 Danelle Cline
Did did you wanna add something?

54:55 Sid Mehta
Oh yeah, sorry, go ahead. Pravin.

54:57 Praveen Palem
Oh yeah. I'm gonna ask a naive question and so you can shut me down if you want to, but since you said you're gonna, you need, you're gonna add university students as external collaborators, I was wondering if, if this, if the data set at least to start with, is safe enough for us also to have to be external collaborators and just just to kind of get the environment set up while you're still exploring and then we can get off of it? Or is that a big no for us to be added? Well help me understand a little bit about, So the idea is for me and potentially maybe said to have access to your environment as external collaborators. Oh, just like the USC or the university students?

55:44 Danelle Cline
Oh, I guess so. I mean, I guess we don't have very many any, we only have five accounts, five seats, so, So yeah. Yeah.

55:55 Sid Mehta
So it might, yeah, it might not be actually, yeah, it might not be, It might be kind of pretty limited for our team. Yeah, Yeah, yeah.

56:03 Danelle Cline
I mean, you know, yeah, Maybe in the short term I think it would be fine. Totally fine. Yeah. If it's helpful.

56:11 Sid Mehta
Yeah, we can, we can see we can, yeah, normally, yeah, normally most customers don't give us access, so we normally don't ask, but it's, you know, it's, it's positive. Like sometimes with these nonprofits they're, they don't mind, sometimes they'll send us data as well. So Exactly.

56:25 Danelle Cline
Just, you know, it's this but no worries if it can't, well I Can make the data public if you would like to, to use it for something. Yeah.

56:32 Sid Mehta
I mean, yeah, this is like something that's open source. It'd always be good because just because sometimes it would be nice like, you know, sometimes if we are running some stuff that we can see it on your data, but again, no pressure to Yeah, but just, yeah, Yeah, it was just the idea, just because you said it's university students are gonna start collaborating, so I thought, you know, hey, why not?

56:50 Praveen Palem
You know?

56:51 Danelle Cline
Well, I mean, to be clear, it, it will be likely not students, but our collaborator who's a researcher in this area and I don't think there, I don't maybe one of his PhD students, so a pretty small group. Got it.

57:15 Sid Mehta
Makes sense.

57:16 Danelle Cline
We would be sharing with, yeah, Got it.

57:19 Praveen Palem
Yeah.

57:19 Sid Mehta
Yeah, if you, yeah, even if you have an open source data set that's like relatively similar, that also works as well.

57:24 Danelle Cline
So like if you have something that you can just direct More about it because, you know, I, I don't see any problem with, with releasing either a subset of the data for, for to, I mean eventually we're gonna share all this data through a public portal and make it probably a public data set. That's the, that's the end goal. But yeah, I don't wanna speak outta turn. It might be too soon. It's, it's prob it's, I mean truthfully it's not my call to make actually, so That's, Let, let me, lemme get back with the team and see what they think.

58:02 Sid Mehta
Yeah, no, no pressure. I think coming up on time, so I know we have like two minutes left. I know we wanted to get like things started on Thursday. Should we do, should we have like a sync on Thursday? So as you guys try stuff you can bring more questions that you might have and then just make there zero weekly think?

58:17 Danelle Cline
I think So we're gonna, we're gonna make some progress between that and them. Okay, cool.

58:21 Sid Mehta
Alright. So I think we can keep the same time as we initially did. I will be out, I'm, I'm leaving on we Wednesday so I'll be out, but Pravin will be there potentially within another colleague. So yeah, cool. They'll be there and then yeah we can, I know it's like a weird time 'cause of the holiday season, so maybe next Thursday I think is also Christmas, so maybe it doesn't make sense to me then, but then we can kind of keep on going with that cadence moving Forward.

58:44 Danelle Cline
Yeah, definitely. Yeah. Well this has been really helpful. I appreciate all of you. I'm super excited to use a tool. I think it's gonna unlock some much more quickly than what we are currently doing to help us iterate on our training and improve our model performance. So that's, that's a win.

59:06 Sid Mehta
Okay, awesome. Cool. Alright, we'll keep chatting and yeah, I probably won't see you guys personally till the end of the year and yeah, so have a happy new Year and Merry Christmas and happy Holidays I guess.

59:18 Danelle Cline
Thank you.

59:19 Praveen Palem
Yeah, Happy holidays. Yeah.

59:20 Danelle Cline
Care.

59:20 Praveen Palem
Talk to you on Thursday.

59:22 Danelle Cline
Okay. Bye-bye.

59:23 Praveen Palem
Yeah, bye Andrew. Nice to meet you both. Bye.
