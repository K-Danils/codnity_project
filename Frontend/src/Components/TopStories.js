import ArticlePodium from './ArticlePodium'

function TopStories({ articles }) {
    const compareValues = (p1, p2) => {
        // used to compare values within the dictionary, compatible with sort function
        return p1["points"] < p2["points"] ? 1 : p1["points"] > p2["points"] ? -1 : 0;
    }
    
    // sort and get top three articles within the dictionary
    const topThreeArticlesByPoints =
        Object.values(articles).sort((a1, a2) => compareValues(a1, a2)).slice(0, 3);

    return (
        <>
            <h2 className='top-story-header'>TOP STORIES RIGHT NOW</h2>

            <div className='article-podium-wrapper row justify-center'>
                <div className='column'>
                    <ArticlePodium
                        article={topThreeArticlesByPoints[1]}
                        placeTitle={"2nd"}
                        animationDelay={0.5}
                    />
                </div>

                <div className='column'>
                    <ArticlePodium
                        article={topThreeArticlesByPoints[0]}
                        placeTitle={"1st"}
                        animationDelay={0}
                    />
                </div>

                <div className='column'>
                    <ArticlePodium
                        article={topThreeArticlesByPoints[2]}
                        placeTitle={"3rd"}
                        animationDelay={0.8}
                    />
                </div>
            </div>
        </>
    );
}

export default TopStories