import { sendToInstagram } from "./instagram.js";
import { sendToTwitter } from "./twitter.js";
import { sendToLinkedIn } from "./linkedin.js";
import { sendToFarcaster } from "./farcaster.js";
import { sendToBlog } from "./blog.js";

export async function distribute(payload) {
  const { profiles, caption, assetUrl } = payload;

  if (profiles.instagram)
    await sendToInstagram(caption, assetUrl);

  if (profiles.twitter)
    await sendToTwitter(caption, assetUrl);

  if (profiles.linkedin)
    await sendToLinkedIn(caption, assetUrl);

  if (profiles.farcaster)
    await sendToFarcaster(caption, assetUrl);

  if (profiles.blog)
    await sendToBlog(caption, assetUrl);

  return { status: "distributed" };
}

