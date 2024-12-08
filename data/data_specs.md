# Product Review Fields

## Bronze layer
Here is a table describing the fields for product review row data:

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rating</td>
      <td>float</td>
      <td>Rating of the product (from 1.0 to 5.0).</td>
    </tr>
    <tr>
      <td>title</td>
      <td>str</td>
      <td>Title of the user review.</td>
    </tr>
    <tr>
      <td>text</td>
      <td>str</td>
      <td>Text body of the user review.</td>
    </tr>
    <tr>
      <td>images</td>
      <td>list</td>
      <td>Images that users post after they have received the product. Each image has different sizes (small, medium, large), represented by the small_image_url, medium_image_url, and large_image_url respectively.</td>
    </tr>
    <tr>
      <td>asin</td>
      <td>str</td>
      <td>ID of the product.</td>
    </tr>
    <tr>
      <td>parent_asin</td>
      <td>str</td>
      <td>Parent ID of the product. Note: Products with different colors, styles, sizes usually belong to the same parent ID. The “asin” in previous Amazon datasets is actually parent ID. <b>Please use parent ID to find product meta.</b></td>
    </tr>
    <tr>
      <td>user_id</td>
      <td>str</td>
      <td>ID of the reviewer.</td>
    </tr>
    <tr>
      <td>timestamp</td>
      <td>int</td>
      <td>Time of the review (unix time).</td>
    </tr>
    <tr>
      <td>verified_purchase</td>
      <td>bool</td>
      <td>User purchase verification.</td>
    </tr>
    <tr>
      <td>helpful_vote</td>
      <td>int</td>
      <td>Helpful votes of the review.</td>
    </tr>
  </tbody>
</table>

## Silver layer
Here is a table describing the fields for product review intermediate data:

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rating</td>
      <td>float</td>
      <td>Rating converted into a range 0 to 1.</td>
    </tr>
    <tr>
      <td>text_aug</td>
      <td>str</td>
      <td>Title and text concatenated, with a space between them.</td>
    </tr>
  </tbody>
</table>

## Gold layer
Here is a table describing the fields for product review final data (to feed the model):

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Type</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rating</td>
      <td>float</td>
      <td>Rating converted into a range 0 to 1.</td>
    </tr>
    <tr>
      <td>text_aug</td>
      <td>str</td>
      <td>Title and text concatenated, with a space between them, lowercase, and without punctuation.</td>
    </tr>
  </tbody>
</table>
