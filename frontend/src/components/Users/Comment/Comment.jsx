import React, { useState } from "react";
import axios from "axios";

import Comments from "@/components/Users/Comment/Comments";
import { useNavigate } from "react-router";

function Comment() {
  const [comment_body, setComment_body] = useState("");
  const [commenter_name, setCommenter_name] = useState("");

  const navigate = useNavigate();

  const AddComment = async () => {
    let formField = new FormData();

    formField.append("comment_body", comment_body);
    formField.append("commenter_name", commenter_name);

    if (comment_body !== null) {
      formField.append("comment_body", comment_body);
    }
    await axios({
      method: "post",
      url: "http://127.0.0.1:8000/comment/",
      data: formField,
    }).then((response) => {
      console.log(response.data);
      navigate.push("/comments");
    });
  };

  return (
    <div className="">
      <div className="flex gap-5 ">
        <img
          src="https://img.freepik.com/free-vector/businessman-character-avatar-isolated_24877-60111.jpg?w=2000"
          alt=""
          className="h-10 w-10 rounded-full "
        />
        <div className="border py-2 px-4 w-full mb-5 rounded-md">
          <form className="">
            <div className="relative flex items-center">
              {/* <SearchIcon className="w-5 h5 absolute text-gray-400" /> */}
              <input
                className="px-7 border-gray-500 outline-none"
                type="text"
                placeholder="Comment"
                value={comment_body}
                onChange={(e) => setComment_body(e.target.value)}
              />
            </div>
          </form>
        </div>
      </div>
      <div className="flex justify-end m">
        <button
          className="flex justify-end btn-default rounded-md px-4 py-1 text-white"
          onClick={AddComment}
        >
          Comment
        </button>
      </div>
      <div>
        <Comments />
      </div>
    </div>
  );
}

export default Comment;
