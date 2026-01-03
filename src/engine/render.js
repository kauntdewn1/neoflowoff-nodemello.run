import { buildImage } from "./buildImage.js";

export async function renderAsset(event) {
  const image = await buildImage(event);
  return image; // path local ou buffer
}

