import cx from "classnames";
import { Component } from "react";

export default class LikeButton extends Component {
  constructor(props) {
    super(props);
    this.state = {
      numberLikes: 100,
      liked: false,
    };
  }

  handleClick = () => {
    if (this.state.liked) {
      this.setState({ liked: false, numberLikes: this.state.numberLikes - 1 });
    } else {
      this.setState({ liked: true, numberLikes: this.state.numberLikes + 1 });
    }
  };
  render() {
    let btnClass = cx("like-button", { liked: this.state.liked });
    return (
      <>
        <div>
          <h2>
            <button class={btnClass} onClick={(e) => this.handleClick()}>
              Like | <span class="likes-counter">{this.state.numberLikes}</span>
            </button>
          </h2>
        </div>
        <style>{`
                    .like-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:  #585858;
                    }
                   .liked {
                        font-weight: bold;
                        color: #1565c0;
                   }
                `}</style>
      </>
    );
  }
}
