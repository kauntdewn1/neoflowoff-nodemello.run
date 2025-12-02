import axios from "axios";

export async function uploadToIPFS(fileBuffer) {
  const endpoint = "https://api.web3.storage/upload";

  const res = await axios.post(endpoint, fileBuffer, {
    headers: {
      "Content-Type": "application/octet-stream",
      "Authorization": `Bearer ${process.env.WEB3_STORAGE_TOKEN}`
    }
  });

  return {
    cid: res.data.cid,
    url: `https://ipfs.io/ipfs/${res.data.cid}`
  };
}

