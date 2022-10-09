function ArticlePodium({ article, placeTitle, animationDelay }) {
  const isFirst = placeTitle == "1st";
  
  return (
    <div
      style={{ height: "100%" }}
      className={isFirst ? "first-place-container" : ""}
      onClick={() => window.open(article.link)}>

      <h2 id={isFirst ? "first-place-points" : "points"}>{article.points}</h2>

      <div
        className={'podium-container ' + (isFirst ? "first-place" : "")}
        style={
          {
            animation: "ease 2s podium-appear forwards",
            animationDelay: animationDelay + "s"
          }
        }>
        <h2>{article.title}</h2>
      </div>

      <h2 id='place-title'>{placeTitle}</h2>

    </div>
  );
}

export default ArticlePodium