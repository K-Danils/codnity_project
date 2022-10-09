import { useEffect, useState } from 'react'
import axios from 'axios';
import TopStories from './TopStories';
import StoryTable from './StoryTable';
import Loader from './Loader';

function MainView() {
    const [articles, setArticles] = useState(undefined);
    const [loading, setLoading] = useState(true);

    const getArticles = () => {
        setLoading(true);

        axios.get("http://localhost:5000/get-articles", {})
            .then(res => setArticles(res.data))
            .catch(err => console.log(err));

        setLoading(false);

    }

    useEffect(() => {
        setArticles(undefined);

        // load articles if they haven't been yet
        if (!articles) {
            getArticles();
        }

    }, [loading]);

    return (
        <div>
            <h1 className='main-header'>Codnity short stories</h1>
            {
                !loading && articles ?
                    <>
                        <TopStories articles={articles} />
                        <StoryTable articles={articles} />
                    </>
                    :
                    <Loader />
            }
        </div>
    );
}

export default MainView