import ReviewsDAO from "../dao/reviewsDAO.js"

export default class ReviewsController {
    static async apiPostReview(req, res, next){
        try{
            const restaurantId = req.body.restaurant_id
            const review = req.body.text
            const userName = req.body.name
            const userId = req.body.user_id
            const now = new Date()

            const reviewResponse = await ReviewsDAO.addReview(restaurantId, userName, userId, review, now)
            res.json({status:"success"})
        } catch(e){
            res.status(500).json({error: e.message})
        }
    }

    static async apiUpdateReview(req, res, next){
        try{
            const reviewId = req.body.review_id
            const review = req.body.text
            const userId = req.body.user_id
            const now = new Date()
            console.log(ReviewsDAO.updateReview)
            const reviewResponse = await ReviewsDAO.updateReview(reviewId, userId, review, now)
            console.log(reviewResponse)
            var {error} = reviewResponse
            if (error) {
                res.status(400).json({error})
            }
            if (reviewResponse.modifiedCount == 0){
                throw new Error("unable to update review - user may not be original poster")
            }
            res.json({status:"success"})
        } catch(e){
            res.status(500).json({error: e.message})
        }
    }
    static async apiDeleteReview(req, res, next){
        try{
            const reviewId = req.query.id
            const userId = req.body.user_id // replace with authentication
            const reviewResponse = await ReviewsDAO.deleteReview(reviewId, userId)
            res.json({status:"success"})
        } catch(e){
            res.status(500).json({error: e.message})
        }
    }
}