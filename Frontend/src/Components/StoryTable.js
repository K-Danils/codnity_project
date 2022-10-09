import DataTable from 'react-data-table-component'
import styled from "styled-components";
import moment from "moment"

function StoryTable({ articles }) {

    // create table with articles
    const columns = [
        {
            name: 'Points',
            selector: row => row.points,
            sortable: true,
            right: true,
            grow: 0,
        },
        {
            name: 'Article title',
            selector: row => row.title,
            sortable: true,
            grow: 3,
        },
        {
            name: "Date",
            selector: row => moment(row.date_created).format("MMMM Do YYYY"),
            sortable: true,
            grow: 1,
        }
    ];

    // set custom style to DataTable
    const Table = styled(DataTable)`
            .rdt_Table{
                background-color:#E8EDDF;
                padding-bottom:10px;
                width:95%;
                margin:auto;
                overflow:hidden;
                border-top-left-radius:10px;
                border-top-right-radius:10px;
            }
            .rdt_TableRow{
                cursor:pointer !important;
                font-size:17px;
                background-color:#E8EDDF;
                font-weight:500;
            }
            .rdt_TableHeadRow{
                font-size:15px;
                font-weight:400;
                background-color:#E8EDDF;
            }
            .rdt_TableRow:hover{
                background-color:#D1D6C3;
            }
        `;

    return (
        <div className='table-container'>
            <div className='table-control-panel-container'>
                <h2>Articles:</h2>
            </div>

            <Table
                columns={columns}
                data={Object.values(articles)}
                onRowClicked={(e) => window.open(e.link)}
            />
        </div>
    );
}

export default StoryTable